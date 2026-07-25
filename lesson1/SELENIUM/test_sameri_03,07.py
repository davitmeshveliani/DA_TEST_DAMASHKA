import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://suninjuly.github.io/cats.html')
    yield driver
    driver.quit()


def test_reder(driver):
   text= driver.find_element(By.CSS_SELECTOR, "[value='Cat memes']").text
   assert text == "Cat memes"

# Написать тест, который проверяет наличия текста "9 mins" в значении времени карточки номер 1



def test_time_value(driver):
    text = driver.find_element(By.CSS_SELECTOR, '[class="col-sm-4"]:nth-child(1) [class="text-muted"]').text
    assert text == "9 mins"


def test_first_card_is_displayed(driver):
    card = driver.find_element(By.CSS_SELECTOR, '[class="col-sm-4"]:nth-child(1)')
    assert card.is_displayed()

def test_third_trie(driver):
    card = driver.find_element(By.CSS_SELECTOR, '[class="col-sm-4"]:nth-child(3)  img')
    assert card.is_displayed()

def test_third_trie(driver):##ormagia  sigrme
    card = driver.find_element(By.CSS_SELECTOR, '[class="col-sm-4"]:nth-child(3)  img')
    third_card = driver.find_element(By.CSS_SELECTOR, '[class="col-sm-4"]:nth-child(3)')
    third_card_image = third_card.find_element(By.TAG_NAME, 'img')
    assert third_card_image.is_displayed()



def test_check_image_quantity(driver):# sigdis shedareba
    images = driver.find_elements(By.TAG_NAME, "img")
    print(f'Изображения {images}')
    print(f'Длина {len(images)}')
    assert len(images) == 6