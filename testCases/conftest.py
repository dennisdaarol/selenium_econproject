from selenium import webdriver
import pytest
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        options = webdriver.ChromeOptions()  #old: driver=webdriver.Chrome()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        options = webdriver.ChromeOptions()  # old: driver=webdriver.Chrome()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    return driver
def pytest_addoption(parser): #this will get the value from CLI /hooks
    parser.addoption("--browser")
@pytest.fixture()
def browser(request): #this will return the browser value to setup method
    return request.config.getoption("--browser")

### PyTest HTML Report  ########
### it is hook for adding Environment info to HTML report
def pytest_configure(config):
    config._metadata = {
        "Tester": "Dennis",
        "Project Name": "HYBRID FRAMEWORK",
    }
    #config._metadata['Project Name'] = 'E sample Commerce'
    #config._metadata['Module Name'] = 'Customers'
    #config._metadata['Tester'] = 'Dennis'

#### It is hook for delete/modify environment information to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)