from classes.Category import Category
import pytest


@pytest.fixture
def category_ovosh():
    return Category('Vegetable', 'eatable product', ['cucumber', 'kabachok'])


def test_init(category_ovosh):
    assert category_ovosh.name == 'Vegetable'
    assert category_ovosh.description == 'eatable product'
    assert category_ovosh.products == ['cucumber', 'kabachok']
