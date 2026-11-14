import geometry
import power_utils

def show_menu():
    print("\n" + "="*30)
    print("ГЛАВНОЕ МЕНЮ")
    print("1. Площадь круга")
    print("2. Площадь прямоугольника")
    print("3. Площадь треугольника")
    print("4. Возведение в степень и сравнение скорости")
    print("0. Выход")
    print("="*30)

def main():
    while True:
        show_menu()
        choice = input("Выберите пункт (0-4): ")

        if choice == '1':
            r = float(input("Введите радиус: "))
            # Используем параметр по умолчанию pi
            print(f"Площадь круга: {geometry.circle_area(r):.2f}")
            
        elif choice == '2':
            a = float(input("Введите длину: "))
            b = float(input("Введите ширину: "))
            print(f"Площадь прямоугольника: {geometry.rectangle_area(a, b):.2f}")
            
        elif choice == '3':
            base = float(input("Введите основание: "))
            h = float(input("Введите высоту: "))
            print(f"Площадь треугольника: {geometry.triangle_area(base, h):.2f}")
            
        elif choice == '4':
            num = float(input("Введите число: "))
            exp = int(input("Введите степень (целое число): "))
            # Вызываем функцию сравнения из второго модуля
            power_utils.compare_performance(num, exp)
            
        elif choice == '0':
            print("Выход из программы. Пока!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()