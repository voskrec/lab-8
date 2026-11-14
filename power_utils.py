import time

def power_recursive(base, exp):
#Рекурсивное возведение в степень.
    if exp == 0:
        return 1
    return base * power_recursive(base, exp - 1)

def power_iterative(base, exp):
#Итеративное возведение в степень.
    result = 1
    for _ in range(exp):
        result *= base
    return result

def compare_performance(base, exp):
#Замеряет время выполнения всех трех способов.
    print(f"\n--- Сравнение скорости для {base}^{exp} ---")
    
    # 1. Рекурсивная
    start = time.perf_counter()
    power_recursive(base, exp)
    print(f"Рекурсивная: {time.perf_counter() - start:.6f} сек.")
    
    # 2. Итеративная
    start = time.perf_counter()
    power_iterative(base, exp)
    print(f"Итеративная: {time.perf_counter() - start:.6f} сек.")
    
    # 3. Встроенная (**)
    start = time.perf_counter()
    base ** exp
    print(f"Встроенная (**): {time.perf_counter() - start:.6f} сек.")