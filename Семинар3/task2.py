# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов

a = [1 ,3, 4, 5, 6, 4, 3, 4, 5, 3, 20, 7, 20, 7]

print(a)


def ununique(input_masive : list[int]):
    set_b = set(a)
    result_massive = []
    for i in set_b:
        if a.count(i) > 1:
            result_massive.append(i)
    return result_massive

print(ununique(a))