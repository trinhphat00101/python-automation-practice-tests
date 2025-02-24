import json
import os

import pytest
from python_practice_automation_test_lib.web_driver.web_driver import WebDriver


@pytest.fixture(scope="session")
def driver(pytestconfig):
    browser_name = pytestconfig.getoption("browser_name")
    driver_options = read_driver_options(browser_name)
    web_driver = WebDriver(browser_name, driver_options).driver
    return web_driver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="wrong browser name")


def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.browser_name
    if 'browser_name' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("browser_name", [option_value])


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
