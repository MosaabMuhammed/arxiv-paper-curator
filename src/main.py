import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger
from my_work.src.config.default_settings import get_settings
# from src.db.factory import make_database
# from src.routers import ask, papers, ping
