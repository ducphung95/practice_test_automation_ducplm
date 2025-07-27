from selenium.webdriver.common.by import By
from base.base_page import BasePage

class InventoryPage(BasePage):
    web_logo = (By.XPATH, "//*[contains(@class, 'app_logo')]")
    hamburger_menu_btn = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    logout_link = (By.XPATH, "//button[@id='logout_sidebar_link']")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    product_title = (By.CLASS_NAME, "title")

    add_to_cart_btn = lambda item_name: (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button[text()='Add to cart']")


    def __init__(self, driver):
        super().__init__(driver)
    
    def get_web_title(self):
        return self.get_text(self.web_logo)
    
    def verify_in_inventory_page(self):
        self.wait_for_element_visible(self.web_logo)
        return "inventory" in self.get_current_url() and self.verify_element_present(self.web_logo)

    def add_item_to_cart(self, item_name):
        item_add_to_cart_locator = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button[text()='Add to cart']")
        self.click(item_add_to_cart_locator)

    def get_cart_item_count(self):
        if self.verify_element_present(self.cart_badge):
            return int(self.get_text(self.cart_badge))
        return 0

    def click_cart_icon(self):
        self.click(self.cart_icon)