"""
Точка входа программы. Здесь вызываются все функции из exceptions_demo.py.
"""

from exceptions_demo import (
    divide,
    withdraw,
    read_file,
    safe_divide,
    process_transaction,
    perform_operations,
    validate_operation,
    simulate_bank_operations,
    simulate_math_operations,
    simulate_file_operations,
)

def run_all():
    """ШАГ 9: Последовательный вызов всех функций с обработкой конкретных исключений."""
    print("=== Демонстрация работы исключений в Python ===\n")

    # Шаг 1
    print("1. Демонстрация divide и withdraw:")
    try:
        print("Результат деления:", divide(10, 0))
    except ZeroDivisionError as e:
        print("Обнаружено исключение:", e)

    try:
        print("Результат снятия:", withdraw(100, 150))
    except ValueError as e:
        print("Обнаружено исключение:", e)

    # Шаг 2
    read_file("unknown.txt")

    # Шаг 3
    print("\nБезопасное деление:")
    print(safe_divide(10, 0))

    # Шаг 4
    print("\nТранзакция:")
    print(process_transaction(100, -50))

    # Шаг 5
    print("\nОперации с числами:")
    print(perform_operations(-2, 3))

    # Шаг 6 + 7
    print("\nПроверка пользовательских исключений:")
    validate_operation("transfer")

    # Шаг 8
    simulate_bank_operations(500)
    simulate_math_operations()
    simulate_file_operations()

    print("\n=== Программа завершена успешно ===")

if __name__ == "__main__":
    run_all()
