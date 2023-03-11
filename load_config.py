"""This module load config value from json file"""
import json
import logging.config

logging.config.fileConfig('loging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def load_config(value: int = 0) -> str | None:
    """Read json config and return string value.
    Value parameter can take two value : 1 - Return path to target folder, 2 - Return printer name"""
    try:
        with open("config.json", "r", encoding="utf-8") as config:
            data = json.load(config)
    except FileNotFoundError:
        logger.error(f'File config.json not found.')
        return None

    match value:
        case 1:
            return data['target_folder']
        case 2:
            return data['printer_name']
