import logging

import pytest
from python_practice_automation_test_lib.web_driver.web_driver import WebDriver

from tests.helper import read_driver_options, get_log_path, CustomFormatter


@pytest.fixture(scope="session")
def driver(pytestconfig):
    browser_name = pytestconfig.getoption("browser_name")
    driver_options = read_driver_options(browser_name)
    web_driver = WebDriver(browser_name, driver_options).driver
    return web_driver


@pytest.fixture(scope="session", autouse=True)
def run_at_end(request, driver):
    def test_case_end():
        # Code to run at the end of the tests
        driver.quit()
    request.addfinalizer(test_case_end)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    log_path = get_log_path()
    logging.basicConfig(
        filename=f'{log_path}',
        level=logging.DEBUG,
        format='[%(asctime)s] %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    console = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    console.setFormatter(CustomFormatter())
    logging.getLogger().addHandler(console)


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="wrong browser name")


def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.browser_name
    if 'browser_name' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("browser_name", [option_value])
