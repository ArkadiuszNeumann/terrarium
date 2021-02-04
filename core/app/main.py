from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from app.routes import (temperature, humidity, relay, door, device, sensor, settings)
import app.utils.database.base.base as base
import app.utils.database.startup.startup as startup
import schedule
from app.config import API_PREFIX
from app.utils.scheduler.scheduler import ScheduleTasks

import asyncio
from app.routes.relay.schema import Relay
from app.routes.relay.job import *


async def startup_handler():
    task = ScheduleTasks()
    asyncio.create_task(task.run())


def bootstrap_app():

    app = FastAPI(title="automated terrarium dashboard API", openapi_prefix=API_PREFIX)


    app.add_event_handler("startup", startup_handler)
    app.include_router(temperature.router, prefix="/sensor")
    app.include_router(humidity.router, prefix="/sensor")
    app.include_router(device.router, prefix="/device")
    app.include_router(sensor.router, prefix="/sensors")
    app.include_router(door.router, prefix="/sensor")
    app.include_router(relay.router, prefix="/relay")
    app.include_router(settings.router, prefix="/settings")
    session = base.session_factory(True)
    startup.migrate(session)
    if __debug__:
        from starlette.middleware.cors import CORSMiddleware
        app.add_middleware(
            CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )
    return app


fastapi_app = bootstrap_app()
