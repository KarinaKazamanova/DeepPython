import random

# axe_x - координаты фигуры по оси х,
# axe_y - координаты фигуры по оси y,
# если представить шахматную доску, как координатную плоскость
def eight_queens(axe_x, axe_y):
    flag = True
    for i in range(8):
        
        diagonal_1 = [(axe_x[i] + k, axe_y[i] + k) for k in range(-8, 9) if (axe_x[i] + k) > 0 and (axe_y[i] + k) > 0]
        diagonal_2 = [(axe_x[i] - k, axe_y[i] + k) for k in range(-8, 9) if (axe_x[i] - k) > 0 and (axe_y[i] + k) > 0]
        vertikal_pos = [(axe_x[i], axe_y[i] + k) for k in range(-8, 9)]
        horisontal_pos = [(axe_x[i] + k, axe_y[i]) for k in range(-8, 9)]
        
        for j in range (i + 1, 8):
            if (axe_x[j], axe_y[j]) in diagonal_1 \
                or (axe_x[j], axe_y[j]) in diagonal_2 \
                or (axe_x[j], axe_y[j]) in vertikal_pos \
                or (axe_x[j], axe_y[j]) in horisontal_pos:
                flag = False
                break    
    return flag


# Если генерить через random.randint(), задача очень долго решается, так как точно известно, что для того 
# чтобы ферзи не пересекались, нужно, чтобы координаты по оси х или по оси у между собой не совпадали 
# (для двухи более ферзей), ты можно сразу генерить листы координат с разными значениями внутри одного листа 
# (все координаты х разные и все координаты у разные, понятно, что в обоих листах координаты пересекаются(лохично :) )
# можно было создать лист или множество уникальных цифр в диапозоне от 1 до 8, 
# а затем его перемешивать отдельно для х и отдельно для у,
# а можно сделать безповторную выборку 8 раз из нужных цифр функцией random.sample
def eight_queens_solution():
    numbers = [1,2,3,4,5,6,7,8]
    count_solutions = 0
    while count_solutions < 4:
        axe_x = random.sample(numbers,8)
        axe_y = random.sample(numbers,8)
        if eight_queens(axe_x, axe_y):
            count_solutions +=1
            print("Удачный вариант ",axe_x, axe_y)
        

eight_queens_solution()

# eight_queens([1,2, 3,4,5,6,7,8], [8,7,6,5,4,3,2,1])
