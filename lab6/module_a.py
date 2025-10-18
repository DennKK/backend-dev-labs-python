"""Шаг 1: Модуль уровня 3 (базовый)"""


def validate_text(text: str) -> bool:
    """Проверка текста"""
    return isinstance(text, str) and len(text) > 0


def calculate_sum(a: float, b: float) -> float:
    """Сложение чисел"""
    return a + b


def format_name(name: str) -> str:
    """Форматирование имени"""
    return name.strip().title()
