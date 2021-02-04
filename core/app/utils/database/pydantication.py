def create_pydantic_object(obj, schema):
    pydantic_object = schema()
    for v in vars(obj):
        for e in vars(pydantic_object):
            if e is v:
                setattr(pydantic_object, e, getattr(obj, v))
    return pydantic_object


def create_db_object(obj, schema, skip=None, **kwargs):
    if skip is None:
        skip = []
    db_object = schema()
    for v in vars(obj):
        if v in skip:
            continue
        setattr(db_object, v, getattr(obj, v))
    if kwargs:
        for key, value in kwargs.items():
            setattr(db_object, key, value)
    return db_object


def edit_db_object(obj, db_object, skip=None):
    if skip is None:
        skip = []
    for v in vars(obj):
        if v in skip:
            continue
        setattr(db_object, v, getattr(obj, v))
    return db_object

