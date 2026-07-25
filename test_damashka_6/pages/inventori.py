from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element_safely(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def add_item_to_cart(self, item_name):
        add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{item_name}']/../../..//button")))
        add_button.click()

    def go_to_cart(self):
        cart_link = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cart_link)
        cart_link.click()