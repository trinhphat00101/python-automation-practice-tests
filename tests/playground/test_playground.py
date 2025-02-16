import pytest
from python_automation_practice_ui.page_object.ui_testing_playground.playground_main_page import PlaygroundMainPage


class TestPlayground:

    @pytest.fixture(scope="module")
    def main_page(self, driver):
        playground_main_page = PlaygroundMainPage(driver)
        yield playground_main_page

    def test_one(self, main_page):
        main_page.open()
