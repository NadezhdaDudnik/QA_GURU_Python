import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_data():
    browser.config.window_height = 1162
    browser.config.window_width = 966
    browser.config.base_url = 'https://google.com'

    yield

    browser.quit()
