def factorial(n: int) -> int:
    if n <= 1:                # База: факториал 1 и 0 равен 1
        return 1              # Останавливаем рекурсию
    
    return n * factorial(n - 1)  # Умножаем n на факториал (n-1)

print(factorial(5))           # 120 (5 * 4 * 3 * 2 * 1)
