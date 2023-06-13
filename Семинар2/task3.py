# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions

import math

def fraction_calc(a, b, c, d):
    frac_sum_1 = int((a * d + c * b) / math.gcd(a * d + c * b, b * d))
    frac_sum_2 = int((b * d) / math.gcd(a * d + c * b, b * d))
    while math.gcd(frac_sum_1, frac_sum_2) > 1:
        frac_sum_1 = int(frac_sum_1 / math.gcd(frac_sum_1, frac_sum_2))
        frac_sum_2 = int(frac_sum_2 / math.gcd(frac_sum_1, frac_sum_2))
    frac_mult_1 = int((a * c) / math.gcd(a * c, b * d))
    frac_mult_2 = int((b * d) / math.gcd(a * c, b * d))
    while math.gcd(frac_mult_1, frac_mult_2) > 1:
        frac_mult_1 = int(frac_mult_1 / math.gcd(frac_mult_1, frac_mult_2))
        frac_mult_2 = int(frac_mult_2 / math.gcd(frac_mult_1, frac_mult_2))

    string_1 = f"{frac_sum_1}/{frac_sum_2}" 
    string_2 =  f"{frac_mult_1}/{frac_mult_2}"
    return string_1, string_2
    


def frac_parse(frac_string):
    new_frac_string = frac_string.split("/")
    return new_frac_string[0], new_frac_string[1]



while True:
    try:
        a, b = (int(i) for i in frac_parse(input("Введите первую дробь ")))
        c, d = (int(i) for i in frac_parse(input("Введите вторую дробь ")))
        print(fraction_calc(a, b, c, d))
        break # Обоснован 
    except:
        print("Вы ввели что-то не то")
         