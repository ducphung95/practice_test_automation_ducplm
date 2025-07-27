from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CheckoutPage(BasePage):
    first_name_field = (By.XPATH, "//input[@id='first-name']")
    last_name_field = (By.XPATH, "//input[@id='last-name']")
    zip_code_field = (By.XPATH, "//input[@id='postal-code']")
    cancel_btn = (By.XPATH, "//button[@id='cancel']")
    continue_btn = (By.ID, "continue")
    
    finish_btn = (By.ID, "finish")
    price_total = (By.CLASS_NAME, "summary_total_label")
    
    complete_header = (By.TAG_NAME, "h2")
    complete_text = (By.CLASS_NAME, "complete-text")
    back_home_btn = (By.XPATH, "//button[@id='back-to-products']")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_in_checkout_step_one(self):
        self.wait_for_element_visible(self.first_name_field)
        return "checkout-step-one" in self.get_current_url()
    
    def enter_first_name(self, first_name):
        self.enter_text(self.first_name_field, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.last_name_field, last_name)

    def enter_zip_code(self, zip_code):
        self.enter_text(self.zip_code_field, zip_code)

    def click_cancel(self):
        self.click(self.cancel_btn) 

    def click_continue(self):
        self.click(self.continue_btn)

    def do_continue(self, first_name, last_name, zip_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)
        self.click_continue()

    def verify_in_checkout_step_two(self):
        self.wait_for_element_visible(self.finish_btn)
        return "checkout-step-two" in self.get_current_url()

    def get_price_total(self):
        return self.get_text(self.price_total)

    def click_finish_button(self):
        self.click(self.finish_btn)

    def verify_complete_header(self):
        header_element = self.wait_for_element_visible(self.complete_header)
        header_text_matches = header_element.text == "Thank you for your order!"
        url_is_correct = "checkout-complete.html" in self.get_current_url()
        return header_text_matches and url_is_correct

    def get_complete_header(self):
        return self.get_text(self.complete_header)
    
    def verify_complete_text(self):
        self.wait_for_element_visible(self.complete_text)
        return "complete-text" in self.get_current_url() and self.verify_element_present(self.complete_text)
    
    def get_complete_text(self):
        return self.get_text(self.complete_text)

    def click_back_home_button(self):
        self.click(self.back_home_btn)