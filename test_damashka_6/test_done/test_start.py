import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_damashka_6.pages.login import LoginPage
from test_damashka_6.pages.inventori import InventoryPage
from test_damashka_6.pages.chekout import CheckoutPage
from test_damashka_6.pages.cart import CartPage

class TestThreeItemsPurchase:
    @pytest.fixture
    def driver(self):
        chrome_options = Options()

        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        yield driver
        driver.quit()

    @pytest.fixture
    def login_page(self, driver):
        return LoginPage(driver)

    @pytest.fixture
    def inventory_page(self, driver):
        return InventoryPage(driver)

    @pytest.fixture
    def cart_page(self, driver):
        return CartPage(driver)

    @pytest.fixture
    def checkout_page(self, driver):
        return CheckoutPage(driver)



    def test_successful_purchase_of_three_items(self, login_page, inventory_page, cart_page, checkout_page):
        login_page.success_login("standard_user", "secret_sauce")
        time.sleep(1)

        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        time.sleep(1)

        inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        time.sleep(1)

        inventory_page.add_item_to_cart("Sauce Labs Onesie")
        time.sleep(1.5)

        inventory_page.go_to_cart()
        time.sleep(1.5)

        cart_page.proceed_to_checkout()
        time.sleep(1)


        checkout_page.fill_checkout_information("Казим", "казизимов", "012357")
        time.sleep(1)


        total_text = checkout_page.get_total_price()
        assert "58.29" in total_text, f"Expected total to contain $58.29, but got '{total_text}'"
        time.sleep(10)


        checkout_page.click_finish()
        time.sleep(1.5)

        success_text = checkout_page.get_success_message()
        assert success_text == "Thank you for your order!", f"Expected 'Thank you for your order!', but got '{success_text}'"