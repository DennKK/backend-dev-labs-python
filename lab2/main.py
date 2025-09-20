def get_numbers():
    """Функция для ввода списка чисел"""
    raw = input("Введите числа через пробел: ")
    return [int(x) for x in raw.split()]

def show_sum(numbers):
    """Функция возвращает сумму элементов"""
    total = 0
    for num in numbers:
        total += num
    return total

def show_min_max(numbers):
    """Функция возвращает минимальное и максимальное число"""
    return min(numbers), max(numbers)

def convert_to_float(numbers):
    """Функция преобразует список чисел в float"""
    return [float(x) for x in numbers]

def filter_even_odd(numbers, even=True):
    """Фильтрация чётных или нечётных чисел"""
    result = []
    for num in numbers:
        if even and num % 2 == 0:
            result.append(num)
        elif not even and num % 2 != 0:
            result.append(num)
    return result

def while_demo():
    """Пример использования цикла while"""
    print("Демонстрация цикла while: вывод чисел от 1 до 5")
    i = 1
    while i <= 5:
        print(i, end=" ")
        i += 1
    print("\n")


def main():
    numbers = get_numbers()

    while True:
        print("\nМеню:")
        print("1 - Найти сумму чисел")
        print("2 - Найти минимальное и максимальное число")
        print("3 - Преобразовать числа в float")
        print("4 - Вывести чётные числа")
        print("5 - Вывести нечётные числа")
        print("6 - Демонстрация цикла while")
        print("0 - Выход")

        choice = input("Выберите действие: ")

        if choice.isdigit():
            choice = int(choice)
        else:
            print("Введите число от 0 до 6")
            continue

        if choice == 1:
            print("Сумма чисел:", show_sum(numbers))
        elif choice == 2:
            mn, mx = show_min_max(numbers)
            print(f"Минимум: {mn}, Максимум: {mx}")
        elif choice == 3:
            floats = convert_to_float(numbers)
            print("Преобразованные в float:", floats)
        elif choice == 4:
            print("Чётные числа:", filter_even_odd(numbers, even=True))
        elif choice == 5:
            print("Нечётные числа:", filter_even_odd(numbers, even=False))
        elif choice == 6:
            while_demo()
        elif choice == 0:
            print("Выход из программы.")
            break
        else:
            print("Нет такого пункта меню.")

if __name__ == "__main__":
    main()
