import os
path = os.path.join(os.getcwd())
print(os.listdir(path))


for item in os.listdir(path):
    if os.path.isfile(item):
        print(f"Файл - " + item)

    elif os.path.isdir(item):
        print("Директория -" + item)
        current_path = str(os.path.realpath(item))  
        print(current_path)

        print(os.listdir(current_path))


# for item in os.listdir(os.path.join(os.getcwd())):
       
#         # file_size = 0
#         # if os.path.isfile(os.path.realpath(item)):
#             parent_directory = str(os.path.join(os.getcwd()))
#             print(item)
#             print(parent_directory)
#             current_path = str(os.path.realpath(item))
#             print("Wefgbds")
#             print(current_path)