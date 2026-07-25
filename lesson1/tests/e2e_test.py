import pytest

@pytest.mark.usefixtures("setup")
class TestInventory:

    def test_backpack_cost(self):
        self.login_page.open()
        self.login_page.success_login("standard_user", "secret_sauce")

        self.inventory_page.add_item_to_cart()
        assert...
