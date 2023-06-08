# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.



def trans(integer):
    result = ""
    symbols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    while integer > 0:
        result += str(symbols[(integer % 16)])  # А что лучше, сразу задать чисто строковый массив или переводить элементы массива с строки, зато не надо будет каждый в кавычки брать?
        integer = integer // 16
    return f"Ox{result[::-1]}"


while True:
    try:
        integer = int(input("Введите число: "))
        result = trans(integer)
        print(result)
        break
    except:
        print("Вы ввели что-то не то")
        continue

