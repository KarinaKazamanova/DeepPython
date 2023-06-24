# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение


import os


def group_renaming(wanted_name,  \
                   old_file_extension, \
                   new_file_extension, \
                   first_old_naming_letter, \
                   last_old_naming_letter, count_of_numbers=3):
    naming_count = "0" * count_of_numbers
    file_count = 1
    for file in (os.listdir()):
        if os.path.isfile(file): 
            initial_name, initial_ext = os.path.join(file).split(".")
            if initial_ext == old_file_extension:
                if file_count < 10 ** count_of_numbers:
                    naming_count = naming_count[:-len(str(file_count))] + str(file_count)
                    final_file_name = initial_name[first_old_naming_letter - 1:last_old_naming_letter] \
                                 + wanted_name + naming_count + "." + new_file_extension
                    os.rename(os.path.join(file), final_file_name)
                    file_count += 1
                else:
                    print("Out of files")
                    break
                
if __name__ == "__main__":
    group_renaming("new_file", "txt", "pdf", 1, 3)