from praktikum.bun import Bun


class TestBun:
    """
        Метод get_name
    """
    def test_get_bun_name(self):
        bun = Bun('Флюоресцентная булка R2-D3', 999)
        bun.get_name()
        assert bun.name == 'Флюоресцентная булка R2-D3'

    """
        Метод price
    """
    def test_get_bun_price(self):
        bun = Bun('Флюоресцентная булка R2-D3', 999)
        bun.get_price()
        assert bun.price == 999

    def test_get_bun_name_and_bun_price(self):
        bun = Bun('Флюоресцентная булка R2-D3', 999)
        assert bun.get_name() == 'Флюоресцентная булка R2-D3'
        assert bun.get_price() == 999
