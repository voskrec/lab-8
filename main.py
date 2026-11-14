def is_prime(n: int) -> bool:
    """Проверяет, является ли число n простым."""
    if n < 2:                 # Числа меньше 2 — не простые
        return False          # Выход: False
    
    for i in range(2, int(n ** 0.5) + 1):  # Идём от 2 до корня из n
        if n % i == 0:        # Если делится без остатка
            return False      # Значит, не простое
    
    return True               # Делителей нет — простое


for num in range(1, 20):      # Числа от 1 до 19
    if is_prime(num):         # Если простое
        print(num, end=" ")   # Печатаем через пробел

# 2 3 5 7 11 13 17 19