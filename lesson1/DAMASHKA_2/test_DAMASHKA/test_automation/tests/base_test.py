import pytest
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.usefixtures("setup")
class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        # ყველა გვერდის ინიციალიზაცია
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

        yield
        self.driver.quit()


class TestSuccessfulPurchase(BaseTest):
    def test_successful_purchase_of_one_item(self):
        # 1. ავტორიზაცია და ნივთის დამატება
        self.login_page.open()
        self.login_page.success_login("standard_user", "secret_sauce")
        time.sleep(2)

        self.inventory_page.add_item_to_cart("Sauce Labs Backpack")
        time.sleep(2)
        # 2. კალათაში გადასვლა და Checkout
        self.inventory_page.go_to_cart()
        self.cart_page.proceed_to_checkout()
        time.sleep(2)

        # 3. მონაცემების შეყვანა
        self.checkout_page.fill_checkout_information("Казим", "казизимов", "012357")
        time.sleep(2)

        # მოლოდინი მეორე გვერდის სრულად ჩატვირთვისთვის
        time.sleep(2)
        # 4. შეკვეთის დასრულება და შემოწმება
        self.checkout_page.click_finish()
        success_text = self.checkout_page.get_success_message().text

        time.sleep(2)
        assert success_text == "Thank you for your order!", f"Expected 'Thank you for your order!', but got '{success_text}'"
        time.sleep(2)