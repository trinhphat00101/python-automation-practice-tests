import json
import logging
import os
from datetime import datetime


def read_driver_options(browser_name):
    current_directory = os.path.abspath(os.path.curdir)
    if browser_name == "chrome":
        json_file_path = os.path.join(current_directory, "tests\\chrome_options.json")
        with open(json_file_path, 'r') as file:
            string_json = file.read()
            data = json.loads(string_json)
            return data
    elif browser_name == "firefox":
        json_file_path = os.path.join(current_directory, "tests\\firefox_options.json")
        with open(json_file_path, 'r') as file:
            string_json = file.read()
            data = json.loads(string_json)
            return data
    elif browser_name == "edge":
        json_file_path = os.path.join(current_directory, "tests\\edge_options.json")
        with open(json_file_path, 'r') as file:
            string_json = file.read()
            data = json.loads(string_json)
            return data


def get_log_path():
    current_directory = os.path.abspath(os.path.curdir)
    now = datetime.now()
    folder_name = now.strftime("%Y-%m-%d_%H-%M-%S")
    os.makedirs(os.path.join(current_directory, f"logs\\{folder_name}"))
    log_path = os.path.join(current_directory, f"logs\\{folder_name}\\selenium.logs")
    return log_path


def step(step_message):
    logger = logging.getLogger()
    logger.info(step_message)


class CustomFormatter(logging.Formatter):
    blue = "\x1b[1;34m"
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: blue + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
