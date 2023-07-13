# 1. Написать программу, которая будет выводить в консоль ёлочку заданной высоты

def print_fir(height):
    for i in range(1, height):
        print(" " * (height - i) + "*" * (2 *  + i - 1) + " " * (height - i) )



while True:
    try:
        height = int(input("Введите желаемую высоту елочки: "))
        print_fir(height)
        break
    except:
        print("Вы ввели что-то не то")
        continue
   

