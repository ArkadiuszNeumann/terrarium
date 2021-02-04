import logging
from sqlalchemy.ext.declarative.clsregistry import _ModuleMarker
from sqlalchemy.orm import RelationshipProperty
from sqlalchemy import inspect
from ..device import Device
from ..door import Door
from ..humidity import Humidity
from ..jobs import Jobs
from ..relay import Relay
from ..sensor import Sensor
from ..settings import Settings
from ..temperature import Temperature


Models = [Device, Door, Humidity, Jobs, Relay, Sensor, Settings, Temperature]
logger = logging.getLogger(__name__)


def migrate(session):
    engine = session.get_bind()
    iengine = inspect(engine)

    db_tables_names = iengine.get_table_names()

    for model in Models:

        if isinstance(model, _ModuleMarker):
            continue

        model_table_name = model.__tablename__
        if model_table_name in db_tables_names:
            model_columns = iengine.get_columns(model_table_name)
            model_columns_names = [c["name"] for c in model_columns]

            mapper = inspect(model)

            for column_prop in mapper.attrs:
                if isinstance(column_prop, RelationshipProperty):
                    pass
                else:
                    for model_column in column_prop.columns:
                        if model_column.key not in model_columns_names:
                            logger.error(f"Model {model} declares column {model_column.key} "
                                         f"which does not exist in database {engine}")
        else:
            logger.error(f"Model {model} declares table {model_table_name} which does not exist in database {engine}")
            model.__table__.create(engine)


async def add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)


    command = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}"

    if column.default is not None:
        is_int = isinstance(column.default.arg, int)
        if is_int:
            command = command + f" DEFAULT {column.default.arg}"
        else:
            command = column + f" DEFAULT '{column.default.arg}'"

    engine.execute(command)