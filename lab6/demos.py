"""Демонстрации"""
from datetime import date
from module_c import register_user, get_user_info
from stdlib_functions import (random_number, random_choice, round_up,
                               round_down, square_root, format_currency,
                               format_number, get_decimal_point,
                               precise_multiply, precise_divide)
from models import Customer, Order
from dataclass_ops import (create_product, update_price, calculate_total,
                           filter_expensive, get_orders_by_customer)


def demo_imports():
    """Шаг 2: Демонстрация импортов"""
    print("\n" + "="*50)
    print("ШАГ 2: ДРЕВОВИДНАЯ СТРУКТУРА ИМПОРТОВ (3 уровня)")
    print("="*50)
    result = register_user("John Doe")
    info = get_user_info(result)
    print(f"Результат: {info}")


def demo_random():
    """Шаг 4: random"""
    print("\n" + "="*50)
    print("ШАГ 4: МОДУЛЬ RANDOM")
    print("="*50)
    print(f"Случайное число: {random_number(1, 100)}")
    print(f"Случайный выбор: {random_choice(['A', 'B', 'C'])}")


def demo_math():
    """Шаг 5: math"""
    print("\n" + "="*50)
    print("ШАГ 5: МОДУЛЬ MATH")
    print("="*50)
    print(f"Округление вверх 3.2: {round_up(3.2)}")
    print(f"Округление вниз 3.8: {round_down(3.8)}")
    print(f"Квадратный корень 16: {square_root(16)}")


def demo_locale():
    """Шаг 6: locale"""
    print("\n" + "="*50)
    print("ШАГ 6: МОДУЛЬ LOCALE")
    print("="*50)
    print(f"Валюта: {format_currency(1234.56)}")
    print(f"Число: {format_number(9876.54)}")
    print(f"Разделитель: {get_decimal_point()}")


def demo_decimal():
    """Шаг 7: decimal"""
    print("\n" + "="*50)
    print("ШАГ 7: МОДУЛЬ DECIMAL")
    print("="*50)
    print(f"Умножение 0.1 * 0.2 = {precise_multiply(0.1, 0.2)}")
    print(f"Деление 1 / 3 = {precise_divide(1, 3)}")


def demo_dataclasses():
    """Шаги 8-9: data-классы"""
    print("\n" + "="*50)
    print("ШАГИ 8-9: DATA-КЛАССЫ")
    print("="*50)

    # 9.5
    p1 = create_product("Laptop", 999.99)
    p2 = create_product("Mouse", 29.99)
    print(f"Создан продукт: {p1.name} - ${p1.price}")

    # 9.1, 9.4
    update_price(p1, 899.99)
    print(f"Обновлена цена: {p1.name} - ${p1.price}")

    # 9.2
    products = [p1, p2]
    print(f"Общая стоимость: ${calculate_total(products)}")

    # 9.2
    expensive = filter_expensive(products, 100)
    print(f"Дорогих товаров: {len(expensive)}")

    # 9.3
    customer = Customer("Alice", "alice@test.com")
    order = Order(p1, customer, date.today(), p1.price)
    orders = {"O001": order}
    by_customer = get_orders_by_customer(orders)
    print(f"Заказы по клиентам: {by_customer}")
