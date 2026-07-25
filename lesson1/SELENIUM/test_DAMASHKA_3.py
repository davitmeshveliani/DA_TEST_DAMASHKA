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
    modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".t-popup_show")))
    assert modal.is_displayed()



def test_check_text_on_page(driver):
    driver.get('https://itcareerhub.de/ru')

    text_container = driver.find_element(By.XPATH, '//*[@id="rec1921708723"]/div/div/div[5]/div')
    expected_text = "Запишитесь на бесплатную консультацию"

    actual_text = text_container.get_attribute("innerText")
    assert expected_text in actual_text, {actual_text}

