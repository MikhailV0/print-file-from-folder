"""This module load config value from json file"""
__author__ = "Mikhail Volokhov"

import json
import logging.config

logging.config.fileConfig('loging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def load_config(value: str, config_file: str = "config.json") -> str | None:
    """Read json config and return string value.
    Value parameter can take any string, if parameter not found in json, return None"""
    try:
        with open(config_file, "r", encoding="utf-8") as config:
            data: dict = json.load(config)
    except FileNotFoundError:
        logger.error(f'File config.json not found.')
        # return None
        raise
    except json.JSONDecodeError as error:
        logger.error(f"Error parsing JSON data in {config_file}: {error}")
        raise

    return data.setdefault(value, None)
