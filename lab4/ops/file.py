"""
Модуль содержит функции для безопасного чтения файлов
и демонстрации работы с файловыми операциями.
"""

# Шаг 2
def read_file(filename):
    """
    Читает содержимое файла с указанным именем.

    Args:
        filename (str): путь к файлу

    Returns:
        str | None: содержимое файла или None при ошибке
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден")
        return None
    except IOError as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

# Шаг 8
def simulate_file_operations():
    """
    Демонстрирует работу функции чтения файлов.
    """
    print("\nРабота с файлами:")
    read_file("non_existing_file.txt")
