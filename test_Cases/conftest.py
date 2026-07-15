import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser Name"
    )


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):

    # Chrome Browser
    if browser.lower() == "chrome":

        options = webdriver.ChromeOptions()

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }

        options.add_experimental_option("prefs", prefs)

        options.add_argument(
            "--disable-blink-features=AutomationControlled"
        )

        driver = webdriver.Chrome(options=options)

    # Firefox Browser
    elif browser.lower() == "firefox":

        driver = webdriver.Firefox()

    # Edge Browser
    elif browser.lower() == "edge":

        driver = webdriver.Edge()

    else:
        raise ValueError(f"Invalid browser: {browser}")

    driver.maximize_window()

    yield driver

    driver.quit()


  #####################################html reports################
  ####### hook for adding envt info in html report
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'Ecommerce Project, nopcommerce'
    config.stash[metadata_key] ['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key] ['Tester Name'] = 'Parag'


    ########################hook for delete and modify envt into html reports

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

