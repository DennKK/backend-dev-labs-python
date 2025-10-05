"""
Модуль содержит функции для безопасного выполнения математических операций,
включая деление с обработкой ошибок и демонстрацию работы функций.
"""

# Шаг 1
def divide(a, b):
    """
    Делит число a на число b.

    Args:
        a (float): делимое
        b (float): делитель

    Returns:
        float: результат деления

    Raises:
        ZeroDivisionError: если b равен 0
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо")
    return a / b

# Шаг 3
def safe_divide(a, b):
    """
    Безопасное деление числа a на число b.
    Если деление на ноль, возвращает 0 и выводит сообщение.

    Args:
        a (float): делимое
        b (float): делитель

    Returns:
        float: результат деления или 0 при ошибке
    """
    result = None
    try:
        if b == 0:
            raise ZeroDivisionError("Попытка деления на ноль")
        result = a / b
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")
    finally:
        if result is None:
            result = 0
            print("Результат установлен по умолчанию = 0")
    return result

# Шаг 5
def perform_operations(a, b):
    """
    Выполняет деление a на b с проверкой на отрицательные числа.
    При ошибках возвращает значение по умолчанию.

    Args:
        a (float): первое число
        b (float): второе число

    Returns:
        float: результат деления, 0 при делении на ноль, 1 при отрицательных числах
    """
    try:
        if a < 0 or b < 0:
            raise ValueError("Числа должны быть положительными")
        result = a / b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
        result = 0
    except ValueError as e:
        print(f"Ошибка данных: {e}")
        result = None
    finally:
        if result is None:
            result = 1
            print("Результат заменён на 1 по умолчанию")
    return result

# Шаг 8
def simulate_math_operations():
    """
    Демонстрирует работу функций безопасного деления.
    """
    print("\nМатематические операции:")
    print(safe_divide(10, 0))
    print(safe_divide(10, 2))
