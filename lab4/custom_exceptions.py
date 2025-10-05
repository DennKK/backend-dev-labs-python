"""
Модуль содержит пользовательские исключения для банковских и математических операций.
"""

class NegativeValueError(Exception):
    """Ошибка: отрицательное значение."""

class NotEnoughFundsError(Exception):
    """Ошибка: недостаточно средств."""

class InvalidOperationError(Exception):
    """Ошибка: некорректная операция."""
