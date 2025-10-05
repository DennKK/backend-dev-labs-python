"""
Модуль содержит функции, демонстрирующие работу исключений в Python.
"""

# === ШАГ 6: Пользовательские исключения ===

class NegativeValueError(Exception):
    """Ошибка, если передано отрицательное значение."""

class NotEnoughFundsError(Exception):
    """Ошибка при недостатке средств на счете."""

class InvalidOperationError(Exception):
    """Ошибка при некорректной операции."""


# === ШАГ 1: Функции без обработчиков исключений ===

def divide(a, b):
    """Шаг 1: Деление чисел, выбрасывает исключение при делении на 0."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо")
    return a / b


def withdraw(balance, amount):
    """Шаг 1: Снятие денег без проверки — выбрасывает исключение при отрицательном балансе."""
    if amount > balance:
        raise ValueError("Недостаточно средств для снятия")
    return balance - amount


# === ШАГ 2: Функция с обработкой конкретных исключений ===

def read_file(filename):
    """Шаг 2: Чтение файла с обработкой ошибок FileNotFoundError и IOError."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден")
        return None
    except IOError as e:
        print(f"Ошибка при чтении файла: {e}")
        return None


# === ШАГ 3: Обработчик конкретного исключения + finally ===

def safe_divide(a, b):
    """Шаг 3: Деление с обработкой ZeroDivisionError и блоком finally."""
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
            print("Устанавливаю результат по умолчанию = 0")
    return result


# === ШАГ 4: Несколько разных обработчиков исключений ===

def process_transaction(balance, amount):
    """Шаг 4: Обработка транзакции с несколькими типами исключений."""
    try:
        if amount < 0:
            raise NegativeValueError("Сумма транзакции не может быть отрицательной")
        if amount > balance:
            raise NotEnoughFundsError("Недостаточно средств")
        result = balance - amount
    except NegativeValueError as e:
        print(f"Ошибка ввода данных: {e}")
        result = balance
    except NotEnoughFundsError as e:
        print(f"Ошибка транзакции: {e}")
        result = balance
    finally:
        print("Транзакция завершена корректно")
    return result


# === ШАГ 5: Генерация и обработка исключений внутри функции ===

def perform_operations(a, b):
    """Шаг 5: Генерация исключений и их обработка внутри функции."""
    result_local = None
    try:
        if a < 0 or b < 0:
            raise NegativeValueError("Оба числа должны быть положительными")
        result_local = a / b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
        result_local = 0
    except NegativeValueError as e:
        print(f"Ошибка данных: {e}")
    finally:
        if result_local is None:
            result_local = 1
            print("Результат заменён на 1 по умолчанию")
    return result_local


# === ШАГ 7: Функция, выбрасывающая пользовательское исключение ===

def validate_operation(op):
    """Шаг 7: Проверка корректности операции. Может выбросить пользовательское исключение."""
    if op not in ("deposit", "withdraw", "check"):
        print(f"Ошибка проверки операции: Некорректная операция: {op}")
    else:
        print(f"Операция '{op}' прошла проверку")
    print("Проверка операции завершена.")


# === ШАГ 8: Три функции, демонстрирующие работу исключений ===

def simulate_bank_operations(balance):
    """Шаг 8: Симуляция банковских операций."""
    print("\nСимуляция банковских операций...")
    balance = process_transaction(balance, 50)
    balance = process_transaction(balance, -10)
    balance = process_transaction(balance, 2000)
    return balance


def simulate_math_operations():
    """Шаг 8: Демонстрация математических исключений."""
    print("\nМатематические операции...")
    print(safe_divide(10, 0))
    print(safe_divide(10, 2))


def simulate_file_operations():
    """Шаг 8: Демонстрация исключений при работе с файлами."""
    print("\nРабота с файлами...")
    read_file("non_existing_file.txt")
