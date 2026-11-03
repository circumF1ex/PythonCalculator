import os
while True:
    os.system("clear") #cls для Windows
    radix = int(input("Введите основание системы (до 10): "))
    if radix < 2 or radix > 9:
        print("Неккоректное основание, повторите ввод (Enter)")
        input()
        continue
        
    a = input(f"Введите число в {radix}-й системе: ")
    #1010 <-
    a_r = a[::-1] 
    #0101 ->
    
    l_a = len(a)    #функция len (length) возвращает
                    #длину последовательности
    summ = 0
    for i in range(l_a):
        summ += int(a_r[i]) * radix**i
    input(f"Число {a} в {radix}-й системе: {summ}")
    break
