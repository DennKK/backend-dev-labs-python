"""Шаг 1: Модуль F"""
from module_b import count_items


def filter_list(items: list, condition) -> list:
    """Фильтрация"""
    return [x for x in items if condition(x)]


def sort_items(items: list) -> list:
    """Сортировка"""
    return sorted(items) if items else []


def list_info(items: list) -> str:
    """Информация о списке"""
    return f"Count: {count_items(items)}"
