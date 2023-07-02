# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# []
# ○Для дочерних объектов указывайте родительскую директорию.
# ○Для каждого объекта укажите файл это или директория.
# ○Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

# os.walk(top, topdown=True, onerror=None, followlinks=False) 

import csv
import json
import os
import pickle


def directory_info(result_dict, path):
    os.chdir(path)
    if os.access(path, mode=7):  
    # if os.path.exists(path):   # print( os.access(path, mode=0o777))
    
        flag = True
        files_size = 0
        for item in os.listdir(path):
            if os.path.isdir(item):
                flag = False

        if flag:
            for item in os.listdir(path):
                parent_directory = str(os.path.join(os.getcwd()))
                if parent_directory in result_dict:
                        result_dict[parent_directory].update({f"{item} - file":os.path.getsize(item)})
                else:
                        result_dict[parent_directory] = {f"{item} - file":os.path.getsize(item)}
                files_size += os.path.getsize(item)
            result_dict[parent_directory].update({f"{parent_directory} - directory":files_size})
            os.chdir(os.pardir)
            

                    
        else:

            list_of_directories = [dir for dir in os.listdir(path) if os.path.isdir(dir)]
            list_of_files = [file for file in os.listdir(path) if os.path.isfile(file)]
            
            parent_directory = str(os.path.join(os.getcwd()))
        
            for item in list_of_files:
                
                if parent_directory in result_dict:
                    result_dict[parent_directory].update({f"{item} - file":os.path.getsize(item)})
                else:
                    result_dict[parent_directory] = {f"{item} - file":os.path.getsize(item)}

                files_size += os.path.getsize(item)
            
            
            for  item in list_of_directories: 
                
                current_path = os.path.realpath(item) 
                directory_info(result_dict, current_path )
                files_size += directory_size(current_path)
            result_dict[parent_directory].update({f"{parent_directory} - directory": files_size})        
                    
                    
        return result_dict
    else:
        print("ВВам отказано в доступе")


   

def write_info(input_dict):
      with (
                 open('list_of_dir_items.json', 'w', encoding='utf-8') as f1,
                 open('list_of_dir_items.csv', 'w', encoding='utf-8') as f2,
                 open('list_of_dir_items.pickle', 'wb') as f3
                 ):
            json.dump(input_dict, f1, ensure_ascii=False,indent=4)
            
          
          
            
           
            for key in input_dict:
                for a_key, a_item in input_dict[key].items():
                    csv_write = csv.DictWriter(f2, fieldnames=[a_key, a_item],
                                dialect='excel',
                                quoting=csv.QUOTE_ALL)
                    csv_write.writeheader()
                    # csv_write.writerow(a_item)
            pickle.dump(input_dict, f3)
              
            


def directory_size(path):
    os.chdir(path)
    result_size = 0
    flag = True
    
    for item in os.listdir():
        if os.path.isdir(item):
            flag = False

    if flag:
        for item in os.listdir():
            result_size += os.path.getsize(item)
        os.chdir(os.pardir)
        return result_size


    else:

        list_of_directories = [dir for dir in os.listdir() if os.path.isdir(dir)]
        list_of_files = [file for file in os.listdir() if os.path.isfile(file)]
        
      
        for item in list_of_files:
            result_size += os.path.getsize(item)
        
        for item in list_of_directories:
            result_size += directory_size(item)
        
        return result_size

#Итоговая функция

def directory_info_in_files(path):
     
    result_dict = {}
    write_info(directory_info(result_dict, path))


directory_info_in_files(os.path.join(os.getcwd()))

