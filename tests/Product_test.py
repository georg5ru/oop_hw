import pytest
from classes.Product import Product

@pytest.fixture
def product_kabachok():
    return Product('Kabachok', 'eatable product, vegetable', 52, 42)

def test_init(product_kabachok):
    assert product_kabachok.name == 'Kabachok'
    assert product_kabachok.description == 'eatable product, vegetable'
    assert product_kabachok.price == 52
    assert product_kabachok.quantity == 42