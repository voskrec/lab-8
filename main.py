import string_utils

# 1. Проверка палиндрома
print(string_utils.is_palindrome("А роза упала на лапу Азора"))  # True
print(string_utils.is_palindrome("Привет"))                      # False

# 2. Проверка анаграммы                   # True
print(string_utils.is_anagram("Слиток", "Листок"))               # True
print(string_utils.is_anagram("Яблоко", "Груша"))                # False

# 3. Подсчёт слов
text = "Python — это очень мощный и удобный язык программирования."
print(string_utils.count_words(text))                            # 8