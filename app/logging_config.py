# app/logging_config.py

import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logging():
    log_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
    os.makedirs(log_directory, exist_ok=True)

    log_file = os.path.join(log_directory, 'app.log')

    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)

    file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
