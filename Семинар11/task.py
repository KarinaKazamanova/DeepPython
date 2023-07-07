
# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц


import datetime


class Square:
    """Класс, содающий прямоугольники"""
    

    def __init__(self, a, b=None):
        
        self.a = a
        if b:
            
            self.b = b
        else:
            
            self.b = a

    def area(self):
        """Функция, находящая площадь"""
        return self.a * self.b
    
    def perimeter(self):
        """Функция, находящая периметр"""
        return 2*(self.a + self.b)
    
    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return Square(new_a, new_b)
    
    def __sub__(self, other):
        if self.a - other.a < 0 or self.b - other.b < 0:
            raise ValueError
        else:
            new_a = self.a - other.a
            new_b = self.b - other.b
            return Square(new_a, new_b)
        
    def __eq__(self, other):
        return self.area() == other.area()
    
    def __gt__(self, other):
        return self.area() > other.area()
    
    def __lt__(self, other):
        return (self.area() <= other.area())
    
    def __le__(self, other):
        return (self.area() >= other.area())
    
if __name__ == "__main__":
    square_1 = Square(10, 6)
    help(Square)


class Mystring(str):
    """Класс """
    def __new__(cls,value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.date = datetime.datetime.now()  # Автоматическое определение времени создания объекта
        return instance