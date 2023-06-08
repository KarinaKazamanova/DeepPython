# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

# В задании сказано только про шестнадтцатиричную систему, но захотелось написать более универсальный метод.


def trans(integer, system):
    result = 0
    sup = 10
    power = 0
    while integer > 0:
        result += (integer % system)*(sup**power)
        power += 1
        integer = integer // system
    return str(result)


while True:
    try:
        integer = int(input("Введите число: "))
        SYSTEM = 16 # Так как в задании указана шестнадцатиричная система, то в качестве констатнты ввела 16, чтобы потом прощебыло менять систему при необходимости
        result = trans(integer,SYSTEM)
        print(result)
        break
    except:
        print("Вы ввели что-то не то")
        continue

