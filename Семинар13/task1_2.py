import math
import turtle

class SideLengthError(Exception):
    def __init__(self, *args):
        self.string = args[0]
        super().__init__(*args)

    def __str__(self):
        return f"Сторона не может быть отрицательной или меньше {self.string}"
    
class TriangleError(Exception):

    def __init__(self, *args):
        self.string = args[0]
        super().__init__(*args)

    def __str__(self):
        return f"Сторона невырожденного треугольника должна быть меньше суммы двух других сторон"
    
class Side():
    def __init__(self, min_value):
        self.min_value = min_value

    def __set_name__(self, owner, name): # length widht
        self.param_name = '_' + name


    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    


    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')
    
    
    def validate(self, value):

        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise SideLengthError(f'{self.min_value}')
        

class Triangle():
    _side_a = Side(0)
    _side_b = Side(0)
    _side_c = Side(0)

    def __init__(self, side_a, side_b, side_c):
        if side_a < side_b + side_c and side_b < side_c + side_a and side_c < side_a + side_b:
            self._side_a = side_a
            self._side_b = side_b
            self._side_c = side_c
        else:
            raise TriangleError("")
        
    @property
    def side_a(self):
        return self._side_a
    
    @property
    def side_b(self):
        return self._side_b
    
    @property
    def side_c(self):
        return self._side_c

    @side_a.setter
    def side_a(self, value):
        if value > 0:
            self._side_a = value
        else:
            raise SideLengthError('0') 
        
    @side_b.setter
    def side_b(self, value):
        if value > 0:
            self._side_b = value
        else:
            raise SideLengthError('0')
        
    @side_c.setter
    def side_c(self, value):
        if value > 0:
            self._side_c = value
        else:
            raise SideLengthError('0')

    

    def __str__(self):
        
        angle_abc = math.degrees(math.acos((self.side_a**2 + self.side_c**2 - self.side_b**2)/(2 * self.side_a * self.side_c)))
        angle_acb = math.degrees(math.acos((self.side_a**2 + self.side_b**2 - self.side_c**2)/(2 * self.side_a * self.side_b)))
        angle_bac = math.degrees(math.acos((self.side_c**2 + self.side_b**2 - self.side_a**2)/(2 * self.side_b * self.side_c)))
        t = turtle.Turtle()
        t.forward(self.side_a)
        t.left(180 - angle_abc)
        t.forward(self.side_c)
        t.left(180 - angle_bac)
        t.forward(self.side_b)
      
       

triangle = Triangle(389,654,786)

print(triangle)


    


    
