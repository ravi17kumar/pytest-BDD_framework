from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time





@pytest.fixture()
def browser():
    chromedriver = "/usr/local/bin/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(chromedriver)
    driver = webdriver.Chrome(service=service, options=options)  # instance of Webdriver
    driver.maximize_window()
    yield driver
    driver.quit()