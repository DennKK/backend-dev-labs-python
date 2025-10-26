"""
Модуль для работы со строками в Python.
Содержит функции для различных операций со строками согласно заданию.
"""

import re
import math


def format_user_profile(name, age, score):
    """
    Функция 1: Форматирование профиля пользователя с подстановкой параметров.
    Принимает имя (строка), возраст (число) и баллы (число).
    Возвращает отформатированную строку с подстановкой значений.
    """
    # Заранее определенная строка-шаблон
    template = "User {name} at age {age} has rating {rating} points"
    
    # Вычисление рейтинга как арифметическая операция
    rating = score * 2 + 10
    
    # Вызов другой функции для получения статуса
    status = get_user_status(rating)
    
    return template.format(name=name, age=age, rating=rating)


def get_user_status(rating):
    """
    Вспомогательная функция для определения статуса пользователя.
    """
    if rating >= 80:
        return "excellent"
    elif rating >= 60:
        return "good"
    else:
        return "beginner"


def generate_password_pattern(base_string, repeat_count):
    """
    Функция 2: Генерация паттерна пароля из повторений базовой строки.
    Выводит каждое повторение на отдельной строке.
    """
    pattern = base_string * repeat_count
    
    print("Generated password pattern:")
    for i in range(repeat_count):
        print(f"Repetition {i+1}: {base_string}")
    
    return pattern


def count_substring_occurrences(text, substring):
    """
    Функция 3: Подсчет количества вхождений подстроки в строку без учета регистра.
    """
    return text.lower().count(substring.lower())


def extract_substring_between_indices(text, start_idx, end_idx):
    """
    Функция 4: Извлечение подстроки между двумя индексами.
    Индексы должны быть больше 0 и меньше длины строки минус 1.
    Тело функции написано в одну строку.
    """
    return text[start_idx:end_idx] if 0 < start_idx < len(text) - 1 and 0 < end_idx < len(text) - 1 and start_idx < end_idx else ""


def find_latin_letters_in_cyrillic_words(*texts):
    """
    Функция 5: Поиск слов с латинскими буквами в текстах с кириллицей.
    Возвращает строки с найденными латинскими символами и количество таких слов.
    """
    # Кириллические буквы, которые визуально неотличимы от латинских
    cyrillic_lookalikes = {
        'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p', 'с': 'c', 'у': 'y', 'х': 'x',
        'А': 'A', 'В': 'B', 'Е': 'E', 'К': 'K', 'М': 'M', 'Н': 'H', 'О': 'O',
        'Р': 'P', 'С': 'C', 'Т': 'T', 'У': 'Y', 'Х': 'X'
    }
    
    latin_words = []
    total_latin_words = 0
    
    for text in texts:
        words = text.split()
        for word in words:
            has_latin = False
            latin_chars = []
            
            for char in word:
                if char.isalpha() and char not in cyrillic_lookalikes and char.isascii():
                    has_latin = True
                    latin_chars.append(char)
            
            if has_latin:
                latin_words.append(f"Word '{word}' contains Latin characters: {', '.join(latin_chars)}")
                total_latin_words += 1
    
    result_text = '\n'.join(latin_words) if latin_words else "No Latin characters found"
    return result_text, total_latin_words


def is_palindrome(text):
    """
    Функция 6: Проверка, является ли строка палиндромом.
    Учитывает как цифры, так и буквы, игнорирует регистр и пробелы.
    """
    # Убираем пробелы и приводим к нижнему регистру
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]


def normalize_spaces(text):
    """
    Функция 7: Нормализация пробелов в строке.
    Убирает пробелы в начале и конце, оставляет по одному пробелу между словами.
    Возвращает длину нормализованной строки.
    """
    normalized = ' '.join(text.split())
    return len(normalized)


def replace_sentence_endings_with_newlines(text):
    """
    Функция 8: Замена знаков окончания предложения на символы переноса строки.
    """
    # Заменяем точки, восклицательные и вопросительные знаки на переносы строк
    result = re.sub(r'[.!?]+', '\n', text)
    return result.strip()
    

def calculate_text_statistics(text):
    """
    Функция 9.1: Расчет статистики текста.
    Возвращает количество слов, символов и предложений.
    """
    words = len(text.split())
    chars = len(text)
    sentences = len(re.findall(r'[.!?]+', text))
    
    return f"Statistics: {words} words, {chars} characters, {sentences} sentences"


def encrypt_caesar_cipher(text, shift):
    """
    Функция 9.2: Шифрование текста шифром Цезаря.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Определяем базовый код для сдвига (латинский алфавит)
            base = ord('a') if char.islower() else ord('A')
            # Применяем сдвиг с учетом алфавита
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result


def find_longest_word(text):
    """
    Функция 9.3: Поиск самого длинного слова в тексте.
    """
    words = text.split()
    if not words:
        return "Text is empty"
    
    longest_word = max(words, key=len)
    return f"Longest word: '{longest_word}' (length: {len(longest_word)} characters)"


def run_all_string_functions():
    """
    Функция 10: Последовательный вызов всех созданных функций.
    Демонстрирует работу всех функций с различными входными данными.
    """
    print("=== DEMONSTRATION OF STRING OPERATIONS IN PYTHON ===\n")
    
    try:
        # Функция 1: Форматирование профиля
        print("1. User profile formatting:")
        profile = format_user_profile("Alexey", 25, 35)
        print(profile)
        print()
        
        # Функция 2: Генерация паттерна пароля
        print("2. Password pattern generation:")
        password_pattern = generate_password_pattern("AbC", 3)
        print(f"Final pattern: {password_pattern}\n")
        
        # Функция 3: Подсчет вхождений подстроки
        print("3. Substring occurrence counting:")
        text = "Python is a great programming language. Python is easy to learn."
        count = count_substring_occurrences(text, "python")
        print(f"Text: {text}")
        print(f"Number of 'python' occurrences (case insensitive): {count}\n")
        
        # Функция 4: Извлечение подстроки
        print("4. Substring extraction between indices:")
        sample_text = "Programming"
        substring = extract_substring_between_indices(sample_text, 2, 8)
        print(f"Text: {sample_text}")
        print(f"Substring between indices 2 and 8: '{substring}'\n")
        
        # Функция 5: Поиск латинских букв
        print("5. Finding Latin letters in Cyrillic words:")
        latin_result, latin_count = find_latin_letters_in_cyrillic_words(
            "Hello world", "Test test", "Cyrillic abc"
        )
        print(latin_result)
        print(f"Total words with Latin letters: {latin_count}\n")
        
        # Функция 6: Проверка палиндрома
        print("6. Palindrome checking:")
        palindromes = ["A man a plan a canal Panama", "12321", "not palindrome"]
        for p in palindromes:
            is_pal = is_palindrome(p)
            print(f"'{p}' - {'palindrome' if is_pal else 'not palindrome'}")
        print()
        
        # Функция 7: Нормализация пробелов
        print("7. Space normalization:")
        messy_text = "   Many    spaces    in   text   "
        normalized_length = normalize_spaces(messy_text)
        print(f"Original text: '{messy_text}'")
        print(f"Length after normalization: {normalized_length}\n")
        
        # Функция 8: Замена знаков препинания
        print("8. Replacing punctuation with newlines:")
        sentences = "First sentence. Second sentence! Third sentence?"
        newlined_text = replace_sentence_endings_with_newlines(sentences)
        print(f"Original text: {sentences}")
        print(f"After replacement:\n{newlined_text}\n")
        
        # Функции 9: Дополнительные алгоритмы
        print("9. Additional string algorithms:")
        
        # 9.1: Статистика текста
        stats = calculate_text_statistics("This is a sample text for analysis. It contains several sentences!")
        print(f"9.1. {stats}")
        
        # 9.2: Шифрование Цезаря
        original = "Hello world"
        encrypted = encrypt_caesar_cipher(original, 3)
        print(f"9.2. Caesar cipher: '{original}' -> '{encrypted}'")
        
        # 9.3: Самое длинное слово
        longest = find_longest_word("Programming in Python is very interesting")
        print(f"9.3. {longest}")
        
        print("\n=== ALL FUNCTIONS EXECUTED SUCCESSFULLY ===")
        
    except Exception as e:
        print(f"Error executing functions: {e}")
        raise
