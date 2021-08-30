from varys.utils import elasticsearch as es
from fastapi import FastAPI
from logging.config import fileConfig

import logging


def create_app():
    _app = FastAPI()
    return _app


app = create_app()
fileConfig('logging.conf')
logger = logging.getLogger()


@app.get('/')
async def index():
    logging.info(es.get_instance().ping(pretty=True))
    return 'Hello World!'
