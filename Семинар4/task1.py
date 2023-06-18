# ✔Напишите функцию для транспонирования матрицы



input_massive = [[1,2,3], [4,5,6], [1,2]]



def transpot_matrix(massive):
    new_matrix = [[0] * len(massive) for i in range(len(massive[0]))]
   
    for i in range(len(massive[0])):
        for j in range(len(massive)):
            new_matrix[i][j] = massive[j][i]
    return new_matrix

print(transpot_matrix(input_massive))