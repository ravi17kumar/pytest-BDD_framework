import pytest
from pytest_bdd import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from driver.drivers import browser
import time
from selenium.webdriver.common.by import By



@given('launching URL in chrome browser')
def launch_browser(browser):
    browser.get('https://app.hubspot.com/login')
    time.sleep(10)

@then('verify that user will redirected to hubspot')
def clicked_element(browser):
    assert browser.find_element(By.LINK_TEXT,"Sign up")

@when('user will able to enter username and pwd so that they will click on login button')
def enter_usrnm_pwd(browser):
    username=browser.find_element(By.ID,"username")
    username.clear
    username.send_keys("test@yopmail.com")
    pwd=browser.find_element(By.ID,"password")
    pwd.clear
    pwd.send_keys("qwerty")
    browser.find_element(By.ID,"loginBtn").click()

@then('verify user is not able to login')
def login_check(browser):
    msg= "This doesn't look right."
    time.sleep(10)
    element=browser.find_element(By.XPATH,"//*[@class='private-alert__inner']/*")
    assert msg==element.text




# @when('user open DemoQa url')
# def openurl():
#     pass





                    