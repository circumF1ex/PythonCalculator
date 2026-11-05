import os
import time
def convert_number():
  while True:
    time.sleep(3)
    os.system('cls')  # Заменено на 'cls', так как вы запускаете в Windows (PS C:\...)
    radix = int(input('Введите радикс (до 10): '))
    if radix < 2 or radix > 9:
      print('Неккоректный радикс, повторите ввод. (Enter)')
      input()
      continue
    a = input(f'Введите число в {radix} системе: ')  # 1010
    a_r = a[::-1]  # 0101
    l_a = len(a)
    summ = 0
    for i in range(l_a):
      summ += int(a_r[i]) * radix**i
    print(a, summ)
    input()
    break