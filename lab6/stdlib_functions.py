"""Шаги 4-7: Стандартные библиотеки"""
import random
import math
import locale
from decimal import Decimal, ROUND_HALF_UP


# Шаг 4: random (2 функции)
def random_number(start: int, end: int) -> int:
    """Случайное число"""
    return random.randint(start, end)


def random_choice(items: list):
    """Случайный выбор"""
    return random.choice(items) if items else None


# Шаг 5: math (3 функции)
def round_up(value: float) -> int:
    """Округление вверх"""
    return math.ceil(value)


def round_down(value: float) -> int:
    """Округление вниз"""
    return math.floor(value)


def square_root(value: float) -> float:
    """Квадратный корень"""
    return math.sqrt(value) if value >= 0 else 0


# Шаг 6: locale (3 функции)
def format_currency(amount: float) -> str:
    """Форматирование валюты"""
    try:
        return locale.currency(amount, grouping=True)
    except (locale.Error, ValueError):
        return f"${amount:.2f}"


def format_number(number: float) -> str:
    """Форматирование числа"""
    try:
        return locale.format_string("%.2f", number, grouping=True)
    except (locale.Error, ValueError):
        return f"{number:.2f}"


def get_decimal_point() -> str:
    """Получение десятичного разделителя"""
    try:
        return locale.localeconv().get("decimal_point", ".")
    except (locale.Error, AttributeError):
        return "."


# Шаг 7: decimal (2 функции)
def precise_multiply(a: float, b: float) -> Decimal:
    """Точное умножение"""
    return (Decimal(str(a)) * Decimal(str(b))).quantize(Decimal('0.01'))


def precise_divide(a: float, b: float) -> Decimal:
    """Точное деление"""
    if b == 0:
        return Decimal('0')
    return (Decimal(str(a)) / Decimal(str(b))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
