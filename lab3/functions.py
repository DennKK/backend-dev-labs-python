"""
Модуль содержит примеры функций для различных случаев:
1) функции без параметров,
2) функции с параметрами и *args/**kwargs,
3) функции с локальными функциями и замыканиями,
4) функции, принимающие другие функции или лямбда-выражения.
"""

# 1. Функция без параметров
def greet():
    """Приветствие пользователя."""
    return "Привет, пользователь!"

# 2. Функция с параметрами
def square(number):
    """Возвращает квадрат числа."""
    return number ** 2

# 3. Функция с несколькими параметрами со значениями по умолчанию
def introduce(name="Гость", age=18):
    """Возвращает строку с именем и возрастом."""
    return f"Имя: {name}, возраст: {age}"

# 4. Функция с несколькими параметрами, у которых задан тип
def add_numbers(a: int, b: int) -> int:
    """Складывает два числа."""
    return a + b

# 5. Функция с неопределённым количеством параметров (*args)
def multiply_all(*args):
    """Перемножает все переданные числа."""
    result = 1
    for num in args:
        result *= num
    return result

# 6. Функция с неопределённым количеством параметров (**kwargs)
def describe_person(**kwargs):
    """Возвращает строку с описанием человека на основе kwargs."""
    return ", ".join(f"{key}: {value}" for key, value in kwargs.items())

# 7. Функция, вызывающая внутри себя другую функцию
def print_greeting_and_square(x):
    """Вызывает greet и square внутри себя."""
    message = greet()
    sq = square(x)
    return f"{message} Квадрат числа {x} = {sq}"

# 8. Функция, принимающая другую функцию как параметр (3 примера)

# Пример 1
def apply_function(func, value):
    """Применяет переданную функцию к значению."""
    return func(value)

# Пример 2
def repeat_action(func, times):
    """Вызывает функцию указанное количество раз."""
    results = [func() for _ in range(times)]
    return results

# Пример 3
def conditional_execute(func_true, func_false, condition):
    """Вызывает одну из функций в зависимости от условия."""
    return func_true() if condition else func_false()

# 9. Функция с объявленной внутри локальной функцией (2 примера)

# Пример 1
def calculator(a, b):
    """Использует внутренние функции для арифметических операций."""
    def add(x, y):
        return x + y

    def multiply(x, y):
        return x * y

    return add(a, b), multiply(a, b)

# Пример 2
def outer_message(name):
    """Создаёт персонализированное сообщение через внутреннюю функцию."""
    def format_message():
        return f"Привет, {name}! Добро пожаловать обратно."

    return format_message()

# 10. Лямбда-выражение без параметров → обычная функция
def lambda_no_params():
    """Функция без параметров, аналог лямбда-выражения."""
    return "Простое лямбда-выражение без параметров"

# 11. Лямбда-выражение с параметрами → обычная функция
def lambda_add(a, b):
    """Функция с параметрами, аналог лямбда-выражения."""
    return a + b

# 12. Функция, принимающая лямбда-выражение как параметр
def process_lambda(func, value):
    """Вызывает переданную функцию с аргументом."""
    return func(value)

# 13. Функции с замыканиями (3 примера)

# Пример 1
def make_multiplier(factor):
    """Возвращает функцию-множитель."""
    def multiplier(x):
        return x * factor
    return multiplier

# Пример 2
def power_of(base):
    """Возвращает функцию, возводящую числа в указанную степень."""
    def power(exp):
        return base ** exp
    return power

# Пример 3
def counter():
    """Создаёт счётчик вызовов."""
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
