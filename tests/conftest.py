import pytest

from Pages.LoginPage import LoginPage


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='Browser test')


@pytest.fixture()
def browser(request):
    select_browser = request.config.getoption('browser').lower()
    if select_browser not in ['chrome', 'firefox', 'safari']:
        select_browser = 'chrome'
    return select_browser


@pytest.fixture()
def setup_login_page(browser):
    login_page = LoginPage(browser=browser)
    yield login_page
    login_page.close()
