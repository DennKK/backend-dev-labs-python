"""
Модуль для запуска всех функций из functions.py и демонстрации их работы.
"""

from functions import greet, square, introduce, add_numbers, multiply_all, describe_person, \
    print_greeting_and_square, apply_function, repeat_action, conditional_execute, \
    calculator, outer_message, lambda_no_params, lambda_add, process_lambda, \
    make_multiplier, power_of, counter

if __name__ == '__main__':

    print(greet())
    print(square(5))
    print(introduce("Денис Карпов", 20))
    print(add_numbers(3, 7))
    print(multiply_all(2, 3, 4))
    print(describe_person(name="Денис", age=20, city="Москва"))
    print(print_greeting_and_square(4))

    # Примеры с функциями как параметрами
    print(apply_function(square, 6))
    print(repeat_action(greet, 3))
    print(conditional_execute(lambda: "Да", lambda: "Нет", True))

    # Внутренние функции
    print(calculator(2, 5))
    print(outer_message("Денис"))

    # Лямбда
    print(lambda_no_params())
    print(lambda_add(4, 5))
    print(process_lambda(lambda x: x * 10, 7))

    # Замыкания
    doubler = make_multiplier(2)
    print(doubler(10))

    cube = power_of(3)
    print(cube(4))

    counter_func = counter()
    print(counter_func())
    print(counter_func())
