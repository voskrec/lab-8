def sum_digits(n: int) -> int:
    # База: если число стало однозначным
    if n < 10:
        return n
    # Шаг: берём последнюю цифру (n % 10) и прибавляем к сумме остальных (n // 10)
    return n % 10 + sum_digits(n // 10)

def reverse_string(s: str) -> str:
    # База: пустая строка или один символ
    if len(s) <= 1:
        return s
    
    # Шаг: берём последний символ (s[-1]) и ставим его перед перевёрнутой остальной частью
    return s[-1] + reverse_string(s[:-1])

def is_palindrome(s: str) -> bool:
    # База: строка из 1 символа или пустая — это палиндром
    if len(s) <= 1:
        return True
        
    # Если первый и последний символы не равны — это не палиндром
    if s[0] != s[-1]:
        return False
        
    # Шаг: отрезаем первый и последний символ и проверяем середину
    return is_palindrome(s[1:-1])

def binary_search(arr: list, target: int, left: int, right: int) -> int:
    # База: границы сошлись, а число не нашли
    if left > right:
        return -1  # -1 значит "не найдено"
        
    # Находим середину
    mid = (left + right) // 2
    
    # Если середина — это наше число, возвращаем его индекс
    if arr[mid] == target:
        return mid
        
    # Шаг: если наше число меньше середины, ищем в левой половине
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
        
    # Шаг: если больше — ищем в правой половине
    else:
        return binary_search(arr, target, mid + 1, right)

# Вызов (нужно передать начало и конец списка):
# binary_search([1, 3, 5, 7, 9], 7, 0, 4)  → вернёт 3 (индекс числа 7)

print(sum_digits(123))
print(reverse_string('popopo'))
print(is_palindrome('pipipipi'))
print(binary_search([1, 3, 5, 7, 9], 7, 0, 4))