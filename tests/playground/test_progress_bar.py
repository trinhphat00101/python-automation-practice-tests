import time

import pytest
from python_automation_practice_ui.page_object.ui_testing_playground.progress_bar_page import ProgressBarPage


class TestProgressBar:

    @pytest.fixture(scope="module")
    def progress_bar_page(self, driver):
        progress_bar_page = ProgressBarPage(driver)
        yield progress_bar_page

    def test_progress_bar_percentage(self, progress_bar_page):
        progress_bar_page.open()
        progress_bar_page.click_start_button()
        time.sleep(5)
        value_progress_bar = progress_bar_page.get_value_of_progress_bar()
        progress_bar_page.click_stop_button()
        assert 50 <= value_progress_bar <= 60, "Progress bar value not correct"
