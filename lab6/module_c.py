"""Шаг 1: Модуль уровня 1"""
from module_b import create_user, check_status


def register_user(name: str) -> dict:
    """Регистрация пользователя"""
    user = create_user(name)
    status = check_status(user)
    return {"user": user, "status": status}


def get_user_info(user_data: dict) -> str:
    """Получение информации"""
    user = user_data.get("user", {})
    return f"User: {user.get('name', 'Unknown')}, Status: {user_data.get('status', 'unknown')}"


def process_data(data: list) -> dict:
    """Обработка данных"""
    return {"count": len(data), "items": data}
