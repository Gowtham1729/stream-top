import logging

from common.config import logging_config


def configure_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create a file handler
    file_handler = logging.FileHandler(logging_config["filename"])
    file_handler.setLevel(logging.INFO)

    # create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging_config["level"])

    # create a formatter and add it to the handlers
    formatter = logging.Formatter(logging_config["format"])
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # add the handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
