from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest
import os


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()

def test_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    user_name = driver.find_element(By.CSS_SELECTOR, "#username")
    user_name.send_keys("davit")

    user_password = driver.find_element(By.CSS_SELECTOR, "#password")
    user_password.send_keys("davit")

    sleep(5)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_data(driver):
    # ბრაუზერის მიმართვა კონკრეტულ მისამართზე (ტესტის საწყისი წერტილი)
    driver.get('https://the-internet.herokuapp.com/login')

    # მომხმარებლის სახელის ველის პოვნა და მასში ტექსტის ჩაწერა
    first_field = driver.find_element(By.ID, 'username')
    first_field.send_keys('tomsmith')
    sleep(1)

    # პაროლის ველის პოვნა და მასში მონაცემების შეყვანა
    second_field = driver.find_element(By.ID, 'password')
    second_field.send_keys('SuperSecretPassword!')

    # შესვლის ღილაკის პოვნა XPath-ით და მასზე დაჭერა)
    login_button = driver.find_element(By.XPATH, '//*[@id="login"]/button')
    login_button.click()

    # წარმატებული ავტორიზაციის შეტყობინების პოვნა (XPath-ის გამოყენებით)
    element = driver.find_element(By.XPATH, '//div[@data-alert="" and @id="flash" and @class="flash success"]')
    print(element.text)

    # ვალიდაცია 1: ვამოწმებთ, გადავიდა თუ არა ბრაუზერი სწორ URL-ზე
    assert driver.current_url == "https://the-internet.herokuapp.com/secure"

    # ვალიდაცია 2: ვამოწმებთ, შეესაბამება თუ არა ეკრანზე გამოტანილი ტექსტი მოლოდინს
    assert "You logged into a secure area!\n×" == element.text
    sleep(1)



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_unsuccessful_login(driver):
    driver.get('https://the-internet.herokuapp.com/login')
    first_field = driver.find_element(By.ID, 'username')
    first_field.send_keys('radomusername')
    second_field = driver.find_element(By.ID, 'password')
    second_field.send_keys('SuperSecretPassword!')
    login_button = driver.find_element(By.CSS_SELECTOR, "#login > button")
    login_button.click()
    element = driver.find_element(By.ID, "flash").text
    print(element)
    assert "Your username is invalid!" in element
    assert driver.current_url == "https://the-internet.herokuapp.com/login"
