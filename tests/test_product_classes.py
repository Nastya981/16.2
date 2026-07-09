"""
Тесты для классов Product и Category
"""

import pytest
from src.product_classes import Product, Category


class TestProduct:
    """Тесты для класса Product"""

    def test_product_initialization(self):
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10


class TestCategory:
    """Тесты для класса Category"""

    def test_category_without_products(self):
        category = Category("Электроника", "Электронные товары")
        assert category.name == "Электроника"
        assert category.description == "Электронные товары"
        assert category.products == []

    def test_category_with_products(self):
        product1 = Product("Телефон", "Смартфон", 50000.0, 10)
        product2 = Product("Ноутбук", "Игровой", 80000.0, 5)
        category = Category("Электроника", "Электронные товары", [product1, product2])
        assert len(category.products) == 2
        assert category.products[0].name == "Телефон"

    def test_category_count(self):
        count_before = Category.category_count
        Category("Кат1", "Описание1")
        Category("Кат2", "Описание2")
        assert Category.category_count == count_before + 2

    def test_product_count(self):
        count_before = Category.product_count
        product1 = Product("Товар1", "Описание1", 100.0, 10)
        product2 = Product("Товар2", "Описание2", 200.0, 5)
        Category("Категория", "Описание", [product1, product2])
        assert Category.product_count == count_before + 2
