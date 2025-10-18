"""Шаг 9: Функции с data-классами"""
from typing import List, Dict
from models import Product, Order


def create_product(name: str, price: float) -> Product:
    """Шаг 9.5: Создание из параметров"""
    return Product(name=name, price=price, quantity=1)


def update_price(product: Product, new_price: float) -> Product:
    """Шаг 9.1 и 9.4: Передача и модификация"""
    product.price = new_price
    return product


def calculate_total(products: List[Product]) -> float:
    """Шаг 9.2: Работа со списком"""
    return sum(p.price * p.quantity for p in products)


def filter_expensive(products: List[Product], min_price: float) -> List[Product]:
    """Шаг 9.2: Фильтрация списка"""
    return [p for p in products if p.price >= min_price]


def get_orders_by_customer(orders: Dict[str, Order]) -> Dict[str, List[str]]:
    """Шаг 9.3: Работа со словарем"""
    result = {}
    for _, order in orders.items():
        name = order.customer.name
        if name not in result:
            result[name] = []
        result[name].append(order.product.name)
    return result
