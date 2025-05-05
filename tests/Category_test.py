from classes.Category import Category
from classes.Product import Product
import pytest


@pytest.fixture
def category_ovosh():
    product_1 = Product("test1", "test2", 10, 100)
    product_2 = Product("test2", "test2", 10, 100)
    return Category('Vegetable', 'eatable product', [product_1, product_2])


def test_init(category_ovosh):
    assert category_ovosh.name == 'Vegetable'
    assert category_ovosh.description == 'eatable product'
    assert category_ovosh.products == ['cucumber', 'kabachok']
    assert Category.category_count == 1
    assert Category.product_count == 2
