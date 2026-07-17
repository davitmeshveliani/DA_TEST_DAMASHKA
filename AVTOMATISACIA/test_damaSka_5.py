#    Задание 1: Проверка наличия текста в iframe

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_iframe_text_task(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"
    driver.get(url)
    sleep(2)

    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)
    sleep(2)

    text_element = driver.find_element(By.TAG_NAME, "body")
    target_text = "semper posuere integer et senectus justo curabitur."

    assert target_text in text_element.text

    driver.switch_to.default_content()
    sleep(2)


# Задание 2: Тестирование Drag & Drop



def test_drag_and_drop_task(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".demo-frame"))


    source = driver.find_element(By.CSS_SELECTOR, "#gallery li:first-child")
    target = driver.find_element(By.ID, "trash")

    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()
    sleep(2)

    trash_items = driver.find_elements(By.CSS_SELECTOR, "#trash li")
    gallery_items = driver.find_elements(By.CSS_SELECTOR, "#gallery li")

    assert len(trash_items) == 1
    assert len(gallery_items) == 3
