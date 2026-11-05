import os, time
enabled = True
os.system('cls')
print('Простой калькулятор.')
def revo(number: str, quad: int) -> str:
    j = len(number) - 1
    sum = 0
    for i in range(len(number)):
        sum += int(number[i]) * (quad**j)
        j = j - 1
    return str(sum)
def any_to_any(number: str, from_base: int, to_base: int) -> str:
    dec_number = int(revo(number, from_base)) # в 10чной системе 141 -> 29

    if dec_number == 0:
        return 0
    
    digits = "0123456789ABCDEF"
    result = ""
    while dec_number > 0:
        result = digits[dec_number % to_base] + result # digits[29 % 7 == 4] = "4" + ""
        dec_number //= to_base # теперь 4
    return result

while enabled:
    print("1. Сложить два числа.")
    print("2. Вычесть два числа.")
    print("3. Умножить два числа.")
    print("4. Разделить число а на в.")
    print("5. Возвести число в степень.")
    print("6. Выход")
    n = input("Введите номер действия: ")
    if (not n.isdigit() or int(n) != 1 and int(n) != 2 and int(n) != 3 and int(n) != 4 and int(n) != 5):
        os.system('cls')
        print("Повторите ввод!")
    else:
        if n == '5':
            a = input("Введите число в любой системе системе: ")
            if (not a.isdigit()):
                os.system('cls')
                print('Повторите ввод!')
                continue
            b = input("Введите степень в которую хотите возвести свое число: ")
            if (not b.isdigit()):
                os.system('cls')
                print('Повторите ввод!')
                continue
            c = input("Введите степень своего переданного числа: ")
            if (not c.isdigit()):
                os.system('cls')
                print('Повторите ввод!')
                continue
            os.system('cls')
            print(f"Число {a} из {c}чной в {b}чной системе счисления: " + any_to_any(a, int(c), int(b)))
        else:
            a = input("Введите число а:")
            if (not a.isdigit()):
                os.system('cls')
                print('Повторите ввод!')
                continue
            b = input("Введите число b:")
            if (not b.isdigit()):
                os.system('cls')
                print('Повторите ввод!')
                continue
            if int(n) == 1:
                os.system('cls')
                print("Результат:", int(a) + int(b))
            elif int(n) == 2:
                os.system('cls')
                print("Результат:", int(a) - int(b))
            elif int(n) == 3:
                os.system('cls')
                print("Результат:", int(a) * int(b))
            elif int(n) == 4:
                os.system('cls')
                print("Результат:", int(a) / int(b))
            elif int(n) == 6:
                print('До скорых встреч!')
                enabled = False
        
