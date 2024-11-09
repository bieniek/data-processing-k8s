import logging

from app.settings import Settings

SETTINGS = Settings()


logging.basicConfig(
    level=SETTINGS.log_level.upper(),
    format="%(asctime)s - %(levelname)s - %(thread)d - %(filename)s:%(funcName)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
