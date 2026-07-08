"""
Модуль с классами Product и Category для интернет-магазина
"""

from typing import List, Optional


class Product:
    """Класс для представления товара"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация товара"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории товаров"""

    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    products: List[Product]

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        """Инициализация категории"""
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.products)
