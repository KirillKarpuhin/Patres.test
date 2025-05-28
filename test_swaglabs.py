import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome() 
    yield driver
    driver.quit() 

link = "https://www.saucedemo.com/"

def test_vhod(browser):
    browser.get(link)

    input1 = browser.find_element(By.ID, "user-name")
    input1.send_keys("standard_user") 

    input2 = browser.find_element(By.ID, "password")
    input2.send_keys("secret_sauce") 

    button = browser.find_element(By.ID, "login-button")
    button.click()

    time.sleep(5)