import os, time
enabled = True
os.system('cls')
import os,time
enabled=True
print('Калькулятор')
enabled2=True
  
while enabled:
    print('1. Сложить два числа +')
    print('2. Вычесть два числа -')
    print('3. Умножить два числа *')
    print('4. Разделить два числа /')
    print('5. Возвести степень **')
    print('6. Разделить без остатка //')
    print('7. Разделить и вывести только остаток %')
    print('8. Система')
    print('9. Выход')
    def convert_number():
        while enabled2:
            os.system('cls')
            radix = int(input('Введите радикс (до 10): '))
            if radix < 2 or radix > 9:
                print('Неккоректный радикс, повторите ввод. (Enter)')
                input()
                continue
            a = input(f'Введите число в {radix} системе: ')
            a_r = a[::-1]
            l_a = len(a)
            summ = 0
            for i in range(l_a):
                summ += int(a_r[i]) * radix**i
            print(summ)
            time.sleep(1)
            os.system('cls')
            break
    n=int(input("Введите номер дейстия: "))
    if n>9:
        print("Некорректный ввод")
        time.sleep(2)
    elif n == 9:
        print("До свидания!")
        time.sleep(2)
        enabled==False
    elif not n==8:
        a=int(input("Введите число a: "))
        b=int(input("Введите число b: "))
    if n == 1:
        print('\n' , a+b, '\n')
        time.sleep(3)
        os.system('cls')
    elif n == 2:
        print('\n' , a-b, '\n')
        time.sleep(3)
        os.system('cls')
    elif n == 3:
        print('\n' , a*b, '\n')
        time.sleep(3)
        os.system('cls')
    elif n == 4:
        print('\n' , a/b, '\n')
        time.sleep(3)
        os.system('cls')
    elif n == 5:
        print('\n' , a**b, '\n')
        time.sleep(3)
        os.system('cls')
    elif n == 6:
        print('\n' , a//b, '\n')
        time.sleep(3)
        os.system('cls')
    elif n == 7:
        print('\n' , a%b, '\n')
        time.sleep(3)
        os.system('cls')
    elif n == 8:
        convert_number()