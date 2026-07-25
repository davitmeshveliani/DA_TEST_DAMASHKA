import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get('https://itcareerhub.de/ru')
    yield driver
    driver.quit()







# დამხარე ფუნქცია ლოდინისთვის (მასალის პრინციპით)
def wait_for_element(driver, locator):
    return WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))


# 1. ლოგო
def test_logo_is_displayed(driver):
    logo = wait_for_element(driver, (By.CSS_SELECTOR, "img.tn-atom__img.t-img"))
    assert logo.is_displayed()


@pytest.mark.parametrize("link_text", ["Программы", "Способы оплаты", "О нас", "Отзывы", "Блог"])
def test_menu_links(driver, link_text):
    link = wait_for_element(driver, (By.LINK_TEXT, link_text))
    assert link.is_displayed()


# 3. ენის გადამრთველები
def test_language_switchers(driver):
    original_url = driver.current_url
    driver.find_element(By.LINK_TEXT, "de").click()
    # ენის შეცვლა იწვევს გვერდის გადატვირთვას, ამიტომ ველოდებით URL-ის ცვლილებას
    WebDriverWait(driver, 10).until(lambda d: d.current_url != original_url)
    assert driver.current_url != original_url


# 4. კონტაქტები
def test_contacts_link(driver):
    contacts = wait_for_element(driver, (By.XPATH, "//*[contains(text(), 'Контакты:')]"))
    time.sleep(6)
    driver.execute_script("arguments[0].scrollIntoView(true);", contacts)
    assert contacts.is_displayed()
    time.sleep(3)

# 5. ღილაკზე დაწკაპუნება და პოპ-აპი
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_callback_and_popup(driver):
    callback_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.t-submit"))
    )
    driver.execute_script("arguments[0].click();", callback_btn)

    time.sleep(5)

    popup_text = "Запишитесь на бесплатную"

    try:
        popup_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{popup_text}')]"))
        )
        assert popup_element.is_displayed()
        print("ტესტი წარმატებულია!")
    except Exception as e:
        print("ტესტი ჩავარდა! მიზეზი:", e)
        driver.save_screenshot("error_popup.png")
        raise
#####################################################



def test_callback_and_popup(driver):
    callback_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.t-submit"))
    )
    driver.execute_script("arguments[0].click();", callback_btn)

    # ანიმაციის ლოდინი
    time.sleep(5)

    # პოპ-აფის ტექსტის შემოწმება
    popup_text = "Запишитесь на бесплатную"
    popup_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{popup_text}')]"))
    )

    # საბოლოო შემოწმება
    assert popup_element.is_displayed(), "პოპ-აფი არ გამოჩნდა!"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_callback_and_popup(driver):
    time.sleep(2)

    callback_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'tn-atom') and contains(text(), 'звонок')]"))
    )

    driver.execute_script("arguments[0].style.border='3px solid red';", callback_btn)

    print("ღილაკი ნაპოვნია ტექსტით:", callback_btn.text)

    driver.execute_script("arguments[0].click();", callback_btn)

    time.sleep(3)
#########################################################

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_language_switchers(driver):
    original_url = driver.current_url

    # ვპოულობთ ელემენტს
    lang_button = driver.find_element(By.LINK_TEXT, "de")

    # 1. ვიზუალური ეფექტი
    driver.execute_script("arguments[0].style.border='3px solid red'", lang_button)

    # 2. კონსოლში ბეჭდვა
    print(f"ვაჭერ ღილაკს: {lang_button.text}")

    lang_button.click()

    WebDriverWait(driver, 10).until(lambda d: d.current_url != original_url)
    assert driver.current_url != original_url



############################

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    driver.quit()


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_callback_flow_contact_page(driver):
    driver.get('https://itcareerhub.de/ru/contact-us')
    callback_btn = driver.find_element(By.XPATH, '//*[@id="rec1194986741"]//a')
    driver.execute_script("arguments[0].click();", callback_btn)

    wait = WebDriverWait(driver, 10)
    modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".t-popup_show")))

    assert modal.is_displayed()


def test_callback_flow(driver):
    driver.get('https://itcareerhub.de/ru')
    # 1. ვპოულობთ ღილაკს
    callback_btn = driver.find_element(By.XPATH, '//*[@id="rec1921708723"]//a')
    driver.implicitly_wait(5)
    # 2. ჩავდივართ ბოლოში და ვაკლიკებთ
    driver.execute_script("arguments[0].scrollIntoView(true);", callback_btn)
    driver.execute_script("arguments[0].click();", callback_btn)
    driver.implicitly_wait(5)
    # 3. ვალიდაცია (მოწმობს, რომ ელემენტი ეკრანზეა)
    assert callback_btn.is_displayed()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


def test_logo_is_displayed(driver):
    driver.get('https://itcareerhub.de/ru')
    assert driver.find_element(By.CSS_SELECTOR, "img.tn-atom__img.t-img").is_displayed()


@pytest.mark.parametrize("link_text", ["Программы", "Способы оплаты", "О нас", "Отзывы", "Блог"])
def test_menu_links(driver, link_text):
    driver.get('https://itcareerhub.de/ru')
    link = driver.find_element(By.LINK_TEXT, link_text)
    assert link.is_displayed()


def test_language_switchers(driver):
    driver.get('https://itcareerhub.de/ru')
    original_url = driver.current_url
    driver.find_element(By.LINK_TEXT, "de").click()
    WebDriverWait(driver, 5).until(lambda d: d.current_url != original_url)
    assert driver.current_url != original_url


def test_contacts_link(driver):
    driver.get('https://itcareerhub.de/ru')
    contacts_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Контакты:')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", contacts_element)
    assert contacts_element.is_displayed()


def test_callback_flow_contact_page(driver):
    driver.get('https://itcareerhub.de/ru/contact-us')
    callback_btn = driver.find_element(By.XPATH, '//*[@id="rec1194986741"]//a')
    driver.execute_script("arguments[0].click();", callback_btn)

    # აქ `wait` მაინც გვჭირდება, რადგან პოპ-აპი დინამიურია და implicitly_wait ყოველთვის არ ყოფნის
    modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".t-popup_show")))
    assert modal.is_displayed()







def test_check_text_on_page(driver):
    driver.get('https://itcareerhub.de/ru')

    text_container = driver.find_element(By.XPATH, '//*[@id="rec1921708723"]/div/div/div[5]/div')
    expected_text = "Запишитесь на бесплатную консультацию"

    actual_text = text_container.get_attribute("innerText")

    assert expected_text in actual_text, {actual_text}

