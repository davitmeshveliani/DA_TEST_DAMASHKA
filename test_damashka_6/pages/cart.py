from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_checkout_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))

    def proceed_to_checkout(self):
        checkout_btn = self.get_checkout_button()

        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkout_btn)

        checkout_btn.click()
