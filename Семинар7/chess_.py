import random


def eight_queens(axe_x, axe_y):
    flag = True
    for i in range(8):
        
        diagonal_pos_1 = [(axe_x[i] + k, axe_y[i] + k) for k in range(-8, 9)]
        diagonal_pos_2 = [(axe_x[i] - k, axe_y[i] + k) for k in range(-8, 9)]
        vertikal_pos = [(axe_x[i], axe_y[i] + k) for k in range(-8, 9)]
        horisontal_pos = [(axe_x[i] + k, axe_y[i]) for k in range(-8, 9)]
        
        for j in range (i + 1, 8):
            if (axe_x[j], axe_y[j]) in diagonal_pos_1 \
                or (axe_x[j], axe_y[j]) in diagonal_pos_2 \
                or (axe_x[j], axe_y[j]) in vertikal_pos \
                or (axe_x[j], axe_y[j]) in horisontal_pos:
                flag = False
                break    
    return flag
        
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
