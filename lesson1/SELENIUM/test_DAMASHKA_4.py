#  Задание 1: Проверка изменения текста кнопки

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


def test_button_text_changes_after_input(driver):
    driver.get('http://uitestingplayground.com/textinput')

    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("ITCH")

    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    wait = WebDriverWait(driver, 5)
    updated_button = wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "ITCH"))
    assert button.text == "ITCH"



####   Задание 2: Проверка загрузки изображений

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_loading_images(driver):
    wait = WebDriverWait(driver, 15)
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
    wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))

    award_image = driver.find_element(By.ID, "award")
    alt_value = award_image.get_attribute("alt")
    assert alt_value == "award"



