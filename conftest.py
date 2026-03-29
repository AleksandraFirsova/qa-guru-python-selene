import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach
from dotenv import load_dotenv

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--browser", default=os.getenv("BROWSER"), help="Browser to use")
    parser.addoption("--browser_version", default=os.getenv("BROWSER_VERSION"), help="Browser version")
    parser.addoption("--headless", default=os.getenv("HEADLESS", "False"), help="Headless mode True/False")
    parser.addoption("--width", default=os.getenv("SCREEN_WIDTH", 1440), help="Window width")
    parser.addoption("--height", default=os.getenv("SCREEN_HEIGHT", 900), help="Window height")
    parser.addoption("--base_url", default=os.getenv("BASE_URL"), help="Base URL")
    parser.addoption("--selenoid_url", default=os.getenv("SELENOID_URL"), help="Selenoid URL")


@pytest.fixture(autouse=True)
def setup_browser(request):
    browser_name = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser_version")
    headless = request.config.getoption("--headless") == "True"
    width = int(request.config.getoption("--width"))
    height = int(request.config.getoption("--height"))
    base_url = request.config.getoption("--base_url")
    selenoid_url = request.config.getoption("--selenoid_url")

    user = os.getenv("SELENOID_USER")
    password = os.getenv("SELENOID_PASSWORD")

    options = Options()
    options.set_capability("browserName", browser_name)
    options.set_capability("browserVersion", browser_version)
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })
    options.add_argument(f"--window-size={width},{height}")

    driver = webdriver.Remote(
        command_executor=f"https://{user}:{password}@{selenoid_url}",
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = base_url
    browser.config.timeout = 10

    yield

    session_id = driver.session_id

    attach.add_screenshot(driver)
    attach.add_page_source(driver)
    attach.add_console_logs(driver)

    driver.quit()
    attach.add_video(session_id)