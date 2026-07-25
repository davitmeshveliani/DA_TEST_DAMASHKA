import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_first_name_input(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

    def get_last_name_input(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "last-name")))

    def get_postal_code_input(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "postal-code")))

    def get_continue_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "continue")))

    def get_finish_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "finish")))

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))

    def enter_first_name(self, first_name):
        field = self.get_first_name_input()
        field.clear()
        field.send_keys(first_name)

    def enter_last_name(self, last_name):
        field = self.get_last_name_input()
        field.clear()
        field.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        field = self.get_postal_code_input()
        field.clear()
        field.send_keys(postal_code)

    def click_continue(self):
        self.get_continue_button().click()

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()

    def click_finish(self):
        time.sleep(1)
        self.get_finish_button().click()