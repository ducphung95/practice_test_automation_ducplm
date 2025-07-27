import pytest
import allure
from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config_reader import ConfigReader
from utils.test_data import checkout_user_info
from utils.test_data import items_to_add_to_cart

@allure.feature("Checkout Process")
@pytest.mark.usefixtures("setup")
class TestCheckout(BaseTest):
    @allure.story("Add items to cart and complete checkout")
    @allure.severity(allure.severity_level.CRITICAL)

    @pytest.fixture(autouse=True)
    def login_precondition(self):
        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)
        
        print("\nPrecondition: Logging in as standard_user...")
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())
        assert inventory_page.verify_in_inventory_page(), "Pre-condition failed: Not on inventory page after login."
        print("Precondition: Successfully logged in.")
        
        yield

    def test_add_3_items_and_finish(self):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        items_to_add = items_to_add_to_cart

        # Add 3 items to the cart
        for item in items_to_add:
            inventory_page.add_item_to_cart(item)
        
        assert inventory_page.get_cart_item_count() == len(items_to_add), \
            f"Expected {len(items_to_add)} items in cart, but found {inventory_page.get_cart_item_count()}"

        # Navigating to Cart page
        inventory_page.click_cart_icon()
        assert cart_page.verify_in_cart_page(), "Failed to navigate to cart page."
        
        for item in items_to_add:
            assert item in cart_page.get_item_names_in_cart(), f"Product '{item}' not found in cart."
        
        cart_page.click_checkout_button()
        assert checkout_page.verify_in_checkout_step_one(), "Failed to navigate to checkout step one."
        
        # Entering user information for checkout
        first_name = checkout_user_info["first_name"]
        last_name = checkout_user_info["last_name"]
        zip_code = checkout_user_info["zip_code"]
        checkout_page.do_continue(first_name, last_name, zip_code)
        assert checkout_page.verify_in_checkout_step_two(), "Failed to navigate to checkout step two (overview)."
        
        checkout_page.click_finish_button()
        assert checkout_page.verify_complete_header(), "Failed to navigate to checkout complete page."
        
        # Verify the confirmation message
        expected_header = "Thank you for your order!"
        expected_text = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

        actual_header = checkout_page.get_complete_header()
        actual_text = checkout_page.get_complete_text()

        assert actual_header == expected_header, \
            f"Validation Failed: Expected header '{expected_header}', but got '{actual_header}'"
        assert actual_text == expected_text, \
            f"Validation Failed: Expected text '{expected_text}', but got '{actual_text}'"
        print("Test purchase completed successfully!")