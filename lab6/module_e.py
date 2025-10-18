"""Шаг 1: Модуль E"""
from module_d import add_numbers


def sum_list(numbers: list) -> float:
    """Сумма списка"""
    result = 0
    for num in numbers:
        result = add_numbers(result, num)
    return result


def average(numbers: list) -> float:
    """Среднее значение"""
    return sum_list(numbers) / len(numbers) if numbers else 0


def max_value(numbers: list) -> float:
    """Максимум"""
    return max(numbers) if numbers else 0
