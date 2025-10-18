"""Шаг 1: Модуль G"""
from module_e import average


def calculate_stats(data: list) -> dict:
    """Статистика"""
    return {"avg": average(data), "count": len(data)}


def normalize(value: float, max_val: float) -> float:
    """Нормализация"""
    return value / max_val if max_val != 0 else 0


def percent(part: float, total: float) -> float:
    """Процент"""
    return (part / total * 100) if total != 0 else 0
