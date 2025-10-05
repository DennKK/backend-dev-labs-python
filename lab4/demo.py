"""
Демонстрационный модуль, показывающий работу функций
и обработку исключений из модулей math, file и bank.
"""

from ops.math import divide, safe_divide, perform_operations, simulate_math_operations
from ops.file import read_file, simulate_file_operations
from ops.bank import withdraw, process_transaction, validate_operation, simulate_bank_operations

def run_all():
    """
    Запускает демонстрацию работы всех функций с обработкой исключений.
    """
    print("=== Демонстрация работы исключений ===\n")

    # Шаг 1
    print("1. Divide и Withdraw:")
    try:
        print("Результат деления:", divide(10, 0))
    except ZeroDivisionError as e:
        print("Исключение:", e)

    try:
        print("Результат снятия:", withdraw(100, 150))
    except ValueError as e:
        print("Исключение:", e)

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
