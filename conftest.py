import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser


@pytest.fixture(autouse=True)
def setup_browser():
    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "127.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })
    options.add_argument("--window-size=1440,900")

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.base_url = "https://demoqa.com"
    browser.config.driver = driver
    browser.config.timeout = 10

    yield
    driver.quit()
