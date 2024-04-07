import pytest
from praktikum.bun import Bun


class TestBun:
    # тест: метод get_name + параметр name
    def test_bun_name_is_correct(self):
        bun = Bun("high-protein", 250)
        assert bun.get_name() == "high-protein"

    # тест: метод get_price + параметр price
    def test_bun_price_is_correct(self):
        bun = Bun("high-protein", 250)
        assert bun.get_price() == 250


