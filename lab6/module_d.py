"""Шаг 1: Дополнительные модули для древовидной структуры"""
from module_a import calculate_sum


def add_numbers(x: float, y: float) -> float:
    """Сложение"""
    return calculate_sum(x, y)


def multiply(x: float, y: float) -> float:
    """Умножение"""
    return x * y


def divide(x: float, y: float) -> float:
    """Деление"""
    return x / y if y != 0 else 0
