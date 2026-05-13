# Task 1
# Напишіть декоратор, який виводить на екран функцію разом із аргументами, що їй передаються.
#УВАГА! Потрібно виводити саму функцію, а не результат її виконання! Наприклад:
# «add викликано з аргументами 4, 5»
# def logger(func):
   # pass
# @logger
# def add(x, y):
   # return x + y
# @logger
# def square_all(*args):
    # return [arg ** 2 for arg in args]
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Формуємо список усіх позиційних та іменованих аргументів
        arg_list = [str(arg) for arg in args]
        kwarg_list = [f"{k}={v}" for k, v in kwargs.items()]
        all_args = ", ".join(arg_list + kwarg_list)
        # Виводимо повідомлення про виклик функції
        print(f"«{func.__name__} викликано з аргументами {all_args}»")
        # Виконуємо оригінальну функцію
        return func(*args, **kwargs)
    return wrapper
# --- Тестування декоратора ---
@logger
def add(x, y):
    return x + y
@logger
def square_all(*args):
    return [arg**2 for arg in args]
# Виклики функцій
add(4, 5)
square_all(1, 2, 3)

# Task 2
# Напишіть декоратор, який приймає список стоп-слів і замінює їх на * всередині декорованої функції
# def stop_words(words: list):
#     pass
# @stop_words([“pepsi”, “BMW”])
# def create_slogan(name: str) -> str:
# return f«{name} п'є пепсі у своєму новенькому BMW!»
# assert create_slogan(«Steve») == «Steve п'є * у своєму новенькому *!»
# Для реалізації декоратора, який приймає аргументи (список стоп-слів), необхідно створити
# трирівневу функцію. Обробка тексту має бути незалежною від регістру букв, щоб надійно
# замінювати слова на зірочки.
# Зовнішня функція stop_words приймає список слів, середня decorator приймає саму функцію, а
# внутрішня wrapper обробляє її аргументи та результат.
# Прапорець re.IGNORECASE гарантує, що слово буде замінено, навіть якщо користувач напише його
# з великої літери (наприклад, "Pepsi" або "bmw").
# функція re.escape: Екранує символи, якщо у списку стоп-слів з'являться знаки на кшталт ?, $, +,
# щоб регулярний вираз не зламався.
from functools import wraps
import re
def stop_words(words: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Викликаємо оригінальну функцію для отримання тексту
            result = func(*args, **kwargs)
            if isinstance(result, str):
                # Замінюємо кожне стоп-слово на "*" без урахування регістру
                for word in words:
                    # re.escape захищає від спецсимволів у словах
                    # flags=re.IGNORECASE дозволяє знаходити і "pepsi", і "пепсі"
                    pattern = re.compile(re.escape(word), re.IGNORECASE)
                    result = pattern.sub("*", result)
            return result
        return wrapper
    return decorator
# --- Тестування декоратора ---
@stop_words(["pepsi", "BMW"])
def create_slogan(name: str) -> str:
    # Оригінальний рядок містить "пепсі" кирилицею та "BMW" латиницею
    return f"{name} п'є pepsi у своєму новенькому BMW!"
# Перевірка роботи за допомогою assert
assert create_slogan("Steve") == "Steve п'є * у своєму новенькому *!"
print("Усі перевірки пройдено успішно!")

# Task 3
# Напишіть декоратор «arg_rules», який перевіряє аргументи, що передаються до функції.
# Декоратор повинен приймати 3 аргументи:
# max_length: 15
# type_: str
# contains: []  — список символів, які повинен містити аргумент
# Якщо перевірка за будь-яким із правил повертає False, функція повинна повернути False
# та вивести причину помилки; в іншому випадку — повернути результат.
# def arg_rules(type_: type, max_length: int, contains: list):
#      pass
# @arg_rules(type_=str, max_length=15, contains=[“05”, “@”])
# def create_slogan(name: str) -> str:
#    return f«{name} п'є пепсі у своєму новенькому BMW!»
# assert create_slogan(“johndoe05@gmail.com”) is False
# assert create_slogan(“S@SH05”) == 'S@SH05 п'є пепсі у своєму новенькому BMW!'
from functools import wraps
def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Перевіряємо всі позиційні та іменовані аргументи
            all_arguments = list(args) + list(kwargs.values())
            for arg in all_arguments:
                # 1. Перевірка типу даних
                if not isinstance(arg, type_):
                    print(
                        f"Помилка валідації: аргумент '{arg}' має тип {type(arg).__name__}, а очікувався {type_.__name__}."
                    )
                    return False
                # 2. Перевірка максимальної довжини
                if len(arg) > max_length:
                    print(
                        f"Помилка валідації: довжина аргументу '{arg}' становить {len(arg)} символів, що перевищує ліміт у {max_length}."
                    )
                    return False
                # 3. Перевірка наявності обов'язкових підрядків/символів
                for substring in contains:
                    if substring not in arg:
                        print(
                            f"Помилка валідації: аргумент '{arg}' не містить обов'язковий елемент '{substring}'."
                        )
                        return False
            # Якщо всі перевірки пройдено, викликаємо оригінальну функцію
            return func(*args, **kwargs)
        return wrapper
    return decorator
# --- Тестування декоратора ---
@arg_rules(type_=str, max_length=15, contains=["05", "@"])
def create_slogan(name: str) -> str:
    return f"{name} п'є пепсі у своєму новенькому BMW!"
# Перевірки за допомогою assert
# 1. Перевищено ліміт довжини (19 символів > 15) -> має повернути False
assert create_slogan("johndoe05@gmail.com") is False
# 2. Усі умови виконано (довжина 6, містить "05" та "@") -> повертає рядок
assert create_slogan("S@SH05") == "S@SH05 п'є пепсі у своєму новенькому BMW!"
print("\nУсі тести та перевірки assert пройдено успішно!")