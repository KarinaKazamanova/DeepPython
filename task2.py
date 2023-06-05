# 2 .Написать порграмму, которая выdодит в консоль таблицу умножения "как на тетрадках"

def multy_table(size):
    
    for i in range(1, 11):
        for j in range(1, size // 2 + 1):
            print(f"{j} x {i} = {i * j}", end= " " * (15 - len(f"{j} x {i} = {i * j}")))
        
        print("\n")

    for i in range(1, 11):
        for j in range(size // 2 + 1, size + 1): 
            print(f"{j} x {i} = {i * j}", end= " " * (15 - len(f"{j} x {i} = {i * j}")))
        print("\n")


height = int(input("введите число: "))
multy_table(height)
