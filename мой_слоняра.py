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
    print("5. Перевести систему счисления в 10-ю.")
    print("6. Выход")

    n = int(input("Введите номер действия: "))

    if 0 < n < 7:
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
            radix = int(input("Введите основание системы (до 10): "))
            if radix < 2 or radix > 9:
                print("Неккоректное основание, повторите ввод (Enter)")
                input()
                continue

            a = input(f"Введите число в {radix}-й системе: ")
            # 1010 <-
            a_r = a[::-1]
            # 0101 ->

            l_a = len(a)  # функция len (length) возвращает
            # длину последовательности
            summ = 0
            for i in range(l_a):
                summ += int(a_r[i]) * radix ** i
            input(f"Число {a} в 10-й системе: {summ}")
            break
        elif n == 6:
            print('До скорых встреч!')
            enabled = False
    else:
        print('Повторите ввод!', end = ' ')
        input("Нажмите Enter чтобы продолжить")