import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_settings():
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1440
    browser.config.window_height = 900
    browser.config.headless = False

    yield

    browser.quit()
