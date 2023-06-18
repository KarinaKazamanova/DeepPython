# ✔Создайте функцию генератор чисел Фибоначчи (см. Википедию).



def Fibonacci_generate(length_of_sequence):
    if length_of_sequence == 1:
        yield 1
    elif length_of_sequence ==  2:
        yield 1
    else:
        yield next(iter(Fibonacci_generate(length_of_sequence - 1))) + next(iter(Fibonacci_generate(length_of_sequence - 2)))



number_imput = 10
for i in range(1, number_imput + 1):
    print(next(iter(Fibonacci_generate(i))))
    