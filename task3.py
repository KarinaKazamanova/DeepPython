# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def is_triangle(a, b, c):
    return (True if a < b + c and b < c + a and c < a + b else False) # Справедливо для невырожденного треугольника. Вырожденный треугольник - треугольник, у которого одна из сторон равна сумме двух других сторон

# Проверка, которая в случае ввода неверного значения заставляет пользователя вводить все три строны заново. 
# Чтобы можно было вводить только дну строну заново, то такую проверку надо делать при каждом вводе отдельно.
while True:
    try:
        a = float(input("Введите первую сторону: "))
        b = float(input("Введите вторую сторону: "))
        c = float(input("Введите третью сторону: "))
        if is_triangle(a, b, c):
            print("Введены стороны невырожденного треугольника")
        else:
            print("Такого треугольника не существует или он вырожден")
        break
    except:
        print("Вы ввели что-то не то")
        continue