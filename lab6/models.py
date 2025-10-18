"""Шаг 8: Data-классы"""
from dataclasses import dataclass
from datetime import date


@dataclass
class Product:
    """Товар"""
    name: str
    price: float
    quantity: int = 0


@dataclass
class Customer:
    """Покупатель"""
    name: str
    email: str
    discount: float = 0.0


@dataclass
class Order:
    """Заказ"""
    product: Product
    customer: Customer
    order_date: date
    total: float = 0.0
