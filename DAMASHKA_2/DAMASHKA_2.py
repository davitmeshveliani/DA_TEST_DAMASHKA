from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def navigate_to_itcareerhub(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(3)


def test_payment_page_navigation(driver):
    navigate_to_itcareerhub(driver)
    find_elements = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    find_elements.click()
    sleep(2)
    driver.save_screenshot("./payment_page.png")


