def n_less10_to_dec(number_str, base):
    """Функция перевода числа из системы счисления с основанием < 10 в десятичную."""
    return int(number_str, base)

def main():
    print("--- Калькулятор систем счисления ---")
    num = input("Введите число: ")
    b = int(input("Введите основание исходной системы (2-9): "))
    
    if 2 <= b < 10:
        result = n_less10_to_dec(num, b)
        print(f"Результат в десятичной системе: {result}")
    else:
        print("Ошибка: Основание должно быть меньше 10 и не меньше 2!")

if __name__ == "__main__":
    main()