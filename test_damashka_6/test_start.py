from data import USER_NAME, PASSWORD, FIRST_NAME, LAST_NAME, POSTAL_CODE

class TestThreeItemsPurchase:

    def test_successful_purchase_of_three_items(self, login_page, inventory_page, cart_page, checkout_page):
        login_page.success_login(USER_NAME, PASSWORD)

        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_item_to_cart("Sauce Labs Onesie")

        inventory_page.go_to_cart()
        cart_page.proceed_to_checkout()

        checkout_page.fill_checkout_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)

        total_text = checkout_page.get_total_price()
        assert "58.29" in total_text, f"Expected total to contain $58.29, but got '{total_text}'"

        checkout_page.click_finish()

        success_text = checkout_page.get_success_message()
        assert success_text == "Thank you for your order!", f"Expected 'Thank you for your order!', but got '{success_text}'"