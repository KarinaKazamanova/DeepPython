# Напишите следующие функции:
# ○Нахождение корней квадратного уравнения
# ○Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


import csv
import json
import random
from functools import wraps
from typing import Callable
from typing import Iterator


def csv_root_finder(func)-> Callable:
    @wraps(func)
    def wrapper(number):
        result_dict = {}
        file = csv_generator("old_file", int(number))
        with open(file, "r", newline="") as file:
            csv_file = csv.DictReader(file, fieldnames=["number_1",
            "number_2", "number_3"], dialect='excel',
            delimiter=' ', quoting=csv.QUOTE_NONNUMERIC)
            result = []
            for line in csv_file:
                for i in line:
                    if type(line[i]) == float:
                       
                       result.append(func(line[i]))
            result_dict[number] = result
        with open("result.json", "a", encoding="utf-8",newline="\n") as res_file:
            json.dump(result_dict, res_file, ensure_ascii=False, indent=4)

        return func

       
    return wrapper


@csv_root_finder
def mathroot(number):
    return number ** 0.5



def csv_generator(file, num_of_rows):
    with open(file, "w", newline="") as csv_file:
        csv_write = csv.DictWriter(csv_file, fieldnames=["number_1",
        "number_2", "number_3"], dialect='excel',
        delimiter=' ', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        dict_row = {}
        for _ in range(num_of_rows):
            dict_row['number_1'] = random.randint(1, 10000)
            dict_row['number_2'] = random.randint(1, 10000)
            dict_row['number_3'] = random.randint(1, 10000)
            csv_write.writerow(dict_row)
    return file


if __name__ == '__main__':
   mathroot(12)