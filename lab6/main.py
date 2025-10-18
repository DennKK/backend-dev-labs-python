"""Лабораторная работа №6"""
from demos import (demo_imports, demo_random, demo_math,
                   demo_locale, demo_decimal, demo_dataclasses)


def run_all():
    """Шаг 10: Главная функция"""
    print("\nЛАБОРАТОРНАЯ РАБОТА №6")
    print("Работа с модулями в Python")

    demo_imports()
    demo_random()
    demo_math()
    demo_locale()
    demo_decimal()
    demo_dataclasses()

    print("\n" + "="*50)
    print("ВЫПОЛНЕНО")
    print("="*50)


if __name__ == "__main__":
    run_all()
