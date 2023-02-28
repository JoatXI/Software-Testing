import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def setup_function(function):
    if os.path.exists("data/vehicles.json"):
        os.remove("data/vehicles.json")
        
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
def test_adding_a_car(driver):
    driver.get("http://127.0.0.1:5000")
    driver.find_element(By.ID, "txtreg").send_keys("ambulance")
    driver.find_element(By.CSS_SELECTOR, "#btnadd").click()
    
    assert driver.find_element("id", "result").text == "Car added successfully"
    
def test_removing_a_car(driver):
    pass