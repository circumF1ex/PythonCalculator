import os, time
enabled = True
os.system('cls')
while enabled:
    os.system('cls')
    print('Простой калькулятор.')
    print("1. Сложить два числа.")
    print("2. Вычесть два числа.")
    print("3. Умножить два числа.")
    print("4. Разделить число а на в.")
    print("5. Выход.")

    n = int(input("Введите номер действия: "))

    if 0 > n > 5:
        a = int(input("Введите число а:"))
        b = int(input("Введите число b:"))
        if n == 1:
            print("Результат:", a + b)
            input("Нажмите Enter чтобы продолжить")
        elif n == 2:
            print("Результат:", a - b)
            input("Нажмите Enter чтобы продолжить")
        elif n == 3:
            print("Результат:", a * b)
            input("Нажмите Enter чтобы продолжить")
        elif n == 4:
            print("Результат:", a / b)
            input("Нажмите Enter чтобы продолжить")
        elif n == 5:
            print('До скорых встреч!')
            enabled = False
    else:
        print('Повторите ввод!', end = ' ')
        input("Нажмите Enter чтобы продолжить")