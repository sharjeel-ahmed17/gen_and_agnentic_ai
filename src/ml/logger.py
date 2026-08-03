import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)
from dotenv import load_dotenv
load_dotenv(override=True)  # Load environment variables from .env file
# Environment variable se name extract karna (Fallback value: "APP_LOG")
MODULE_NAME = os.getenv("LOG_MODULE_NAME", "APP_LOG")


def get_logger(logger_name=MODULE_NAME):
    """Environment variable ke basis par dynamic logger generate karta hai."""
    today_date = datetime.now().strftime("%Y-%m-%d")

    # Dynamic file path based on Env Var
    log_file_path = os.path.join(LOGS_DIR, f"{logger_name}_{today_date}.log")

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = TimedRotatingFileHandler(
            log_file_path,
            when="midnight",
            interval=1,
            backupCount=30,
            encoding="utf-8",
        )
        file_handler.suffix = "%Y-%m-%d"

        formatter = logging.Formatter(
            "[ %(asctime)s ] %(filename)s:%(lineno)d %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger


# Dynamic Logger Initialization
logger = get_logger()


def log_info(message):
    logger.info(message)


def log_warning(message):
    logger.warning(message)


def log_error(message):
    logger.error(message)


def log_debug(message):
    logger.debug(message)


if __name__ == "__main__":
    log_info("Logger environment variable se load ho gaya hai.")