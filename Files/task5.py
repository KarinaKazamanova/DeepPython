# 4. Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
import random


# Number - искомое число, tries -количество попыток
def guess(number, tries, maximum, minimum):
    
    
    while tries:
        random_number = random.randint(minimum ,maximum )
        print (f"попытка {10 - tries + 1}: {random_number}")
        if random_number == number:
            print("Я угадал!")
            break
        else:
            if random_number > number:
                maximum = random_number
                tries -= 1
                continue
                
            else:
                minimum = random_number
                tries -= 1
                continue          
    else:
        print("Я не смог угадать")

while True:
    try:

        input_number = int(input("Введите число "))
        guess(input_number, 10, 1000, 0)
        break
    except:
        print("Вы ввели что-то не то")
        continue
