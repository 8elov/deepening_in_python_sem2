# Напишите программу,
# которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions


def find_gcd(a, b):
    """Function finds the greatest common divisor"""
    while b != 0:
        a, b = b, a % b
    return a


def simplify_fraction(numerator, denominator):
    """Function reduces the fraction to the minimum manifested form"""
    common_divisor = find_gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor


def add_fractions(fraction1, fraction2):
    """Function to add fractions"""
    num1, den1 = map(int, fraction1.split("/"))
    num2, den2 = map(int, fraction2.split("/"))

    common_denominator = den1 * den2
    new_num1 = num1 * den2
    new_num2 = num2 * den1

    sum_numerators = new_num1 + new_num2
    return simplify_fraction(sum_numerators, common_denominator)


def multiply_fractions(fraction1, fraction2):
    """Function multiplies fractions"""
    num1, den1 = map(int, fraction1.split("/"))
    num2, den2 = map(int, fraction2.split("/"))

    product_numerator = num1 * num2
    product_denominator = den1 * den2
    return simplify_fraction(product_numerator, product_denominator)


first_fraction = input("Введите первую дробь в формате a/b: ")
second_fraction = input("Введите вторую дробь в формате a/b: ")

sum_result = add_fractions(first_fraction, second_fraction)
product_result = multiply_fractions(first_fraction, second_fraction)

print(f"Сумма дробей: {sum_result[0]}/{sum_result[1]}")
print(f"Произведение дробей: {product_result[0]}/{product_result[1]}")

f1 = fractions.Fraction(int(first_fraction[0]), int(first_fraction[2]))
f2 = fractions.Fraction(int(second_fraction[0]), int(second_fraction[2]))
print(f"Сумма дробей: {f1 + f2}")
print(f"Произведение дробей: {f1 * f2}")
