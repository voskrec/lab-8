# Файл: math_ops.py

def add(a, b):
    # Сложение
    return a + b

def subtract(a, b):
    # Вычитание
    return a - b

def multiply(a, b):
    # Умножение
    return a * b

def divide(a, b):
    # Деление с проверкой на ноль
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b