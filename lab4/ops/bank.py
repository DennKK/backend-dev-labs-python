"""
Модуль содержит функции для работы с банковскими операциями,
включая снятие средств, обработку транзакций и проверку операций.
"""

# Шаг 1
def withdraw(balance, amount):
    """
    Выполняет снятие указанной суммы с баланса.

    Args:
        balance (float): текущий баланс
        amount (float): сумма для снятия

    Returns:
        float: новый баланс после снятия

    Raises:
        ValueError: если сумма превышает баланс
    """
    if amount > balance:
        raise ValueError("Недостаточно средств")
    return balance - amount

# Шаг 4
def process_transaction(balance, amount):
    """
    Обрабатывает транзакцию снятия средств с проверкой на отрицательные суммы
    и недостаточный баланс.

    Args:
        balance (float): текущий баланс
        amount (float): сумма для снятия

    Returns:
        float: новый баланс после транзакции
    """
    try:
        if amount < 0:
            raise ValueError("Отрицательная сумма")
        if amount > balance:
            raise ValueError("Недостаточно средств")
        result = balance - amount
    except ValueError as e:
        print(f"Ошибка транзакции: {e}")
        result = balance
    finally:
        print("Транзакция завершена")
    return result

# Шаг 7
def validate_operation(op):
    """
    Проверяет корректность операции банка.

    Args:
        op (str): операция ('deposit', 'withdraw', 'check')
    """
    if op not in ("deposit", "withdraw", "check"):
        print(f"Ошибка проверки операции: Некорректная операция: {op}")
    else:
        print(f"Операция '{op}' корректна")
    print("Проверка завершена.")

# Шаг 8
def simulate_bank_operations(balance):
    """
    Демонстрирует работу функций обработки банковских транзакций.

    Args:
        balance (float): начальный баланс

    Returns:
        float: баланс после всех транзакций
    """
    print("\nСимуляция банковских операций:")
    balance = process_transaction(balance, 50)
    balance = process_transaction(balance, -10)
    balance = process_transaction(balance, 2000)
    return balance
