# Напишите программу,
# которая получает целое число и возвращает его шестнадцатеричное
# строковое представление.
# Функцию hex используйте для проверки своего результата.

HEXADEMICAL = 16
HEX_MAP = "0123456789abcdef"


def hex_func(number):
    """Function converts a number to hexadecimal"""
    if number == 0:
        return "0"
    else:
        hexadecimal_number = ''
        while number != 0:
            remainder = number % HEXADEMICAL
            hexadecimal_number = HEX_MAP[remainder] + hexadecimal_number
            number //= HEXADEMICAL
        return hexadecimal_number


number = int(input("Введите число: "))
print(hex_func(number))
print(hex(number)[2:])
