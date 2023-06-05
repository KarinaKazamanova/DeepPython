# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def is_triangle(a, b, c):
    return (True if a < b + c & b < c + a & c < a + b else False) # Справедливо для невырожденного треугольника. Вырожденный треугольник - треугольник, у которого одна из сторон равна сумме двух других сторон


while True:
    try:
        a = int(input("Введите первую сторону: "))
        b = int(input("Введите вторую сторону: "))
        c = int(input("Введите третью сторону: "))
        if is_triangle(a, b, c):
            print("Введены стороны невырожденного треугольника")
        else:
            print("Такого треугольника не существует или он вырожден")
        break
    except:
        continue