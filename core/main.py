#! /usr/bin/env python3
from fastapi.logger import logger
import uvicorn
import logging
from app import fastapi_app

gunicorn_logger = logging.getLogger('gunicorn.debug')
logger.handlers = gunicorn_logger.handlers

if __name__ == "__main__":
    logger.setLevel(gunicorn_logger.level)
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)
else:
    logger.setLevel(logging.DEBUG)
