"""Шаг 1: Модуль уровня 2"""
from module_a import validate_text, format_name


def create_user(name: str) -> dict:
    """Создание пользователя"""
    if validate_text(name):
        return {"name": format_name(name), "active": True}
    return {}


def check_status(user: dict) -> str:
    """Проверка статуса"""
    return "active" if user.get("active") else "inactive"


def count_items(items: list) -> int:
    """Подсчет элементов"""
    return len(items) if items else 0
