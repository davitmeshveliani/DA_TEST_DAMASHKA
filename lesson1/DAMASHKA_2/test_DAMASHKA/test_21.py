import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture
def setup_browser():
    # ავტომატურად პოულობს და აინსტალირებს Chrome-ის დრაივერს
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_payment_methods_section(setup_browser):
    driver = setup_browser
    driver.get("https://itcareerhub.de/ru")

    time.sleep(3)

    # "Способы оплаты"-ზე გადასვლა
    payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_link.click()

    time.sleep(2)

    # სკრინშოტი
    driver.save_screenshot("payment_methods.png")