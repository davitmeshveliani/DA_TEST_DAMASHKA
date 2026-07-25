import pytest
from selenium import webdriver
from Lesson6.pages.login_page import LoginPage
from Lesson6.pages.inventory_page import InventoryPage
from Lesson6.pages.cart_page import CartPage


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    request.cls.inventory_page = InventoryPage(driver)
    request.cls.cart_page = CartPage(driver)

    yield
    driver.quit()
