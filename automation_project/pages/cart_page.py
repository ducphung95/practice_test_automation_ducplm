from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class CartPage(BasePage):
    cart_item = (By.CLASS_NAME, "cart_item")
    checkout_btn = checkout_btn = (By.XPATH, "//button[@id='checkout']")
    continue_shopping_btn = (By.XPATH, "//button[@id='continue-shopping']")
    inventory_item_name = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_in_cart_page(self):
        WebDriverWait(self.driver, self.timeout).until(EC.url_contains("cart.html"))
        return "cart" in self.get_current_url()

    def get_cart_items_count(self):
        items = self.driver.find_elments(*self.cart_item)
        return len(items)

    def get_item_names_in_cart(self):
        item_elements = self.driver.find_elements(*self.inventory_item_name)
        return [element.text for element in item_elements]

    def click_checkout_button(self):
        self.click(self.checkout_btn)

    def remove_item_from_cart(self, item_name):
        remove_button_locator = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='cart_item']//button[text()='Remove']")
        self.click(remove_button_locator)