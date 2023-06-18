# ✔Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os



def get_file_info(path):
    return path, path.split("\\")[-1], path.split("\\")[-1].split(".")[-1]

print(get_file_info(os.path.abspath('task1.txt')))