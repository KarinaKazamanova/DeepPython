# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
# Напишите к ним классы исключения с выводом подробной информации. 
# Поднимайте исключения внутри основного кода. 
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.
class LengtWidghtError(Exception):
    def __init__(self, *args):
        self.string = args[0]
        super().__init__(*args)

    def __str__(self):
        return f"Сторона прямоугольника не может быть меньше или равно {self.string}" 


class Value:

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
            raise LengtWidghtError(f'{self.min_value}')

class Square:

    # __slots__ = ["_length", "_widht"]
    _length = Value(1)
    _widht = Value(1)

    def __init__(self, a, b=None):
        
        self._length = a
        if b:
            
            self._widht = b
        else:
            
            self._widht = a


    @property
    def length(self):
        return self._length
    @property
    def wight(self):
        return self._widht

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise LengtWidghtError('0') 
        
    @wight.setter
    def wight(self, value):
        if value > 0:
            self._widht = value
        else:
            raise LengtWidghtError('0') 

    
    def square(self):
        return self._length * self._widht
    
    def perimeter(self):
        return 2*(self._length + self._widht)
    
sq = Square(1,2) # Дискриптор работает только при создании
print(sq.square())
print(sq.perimeter())    
sq.length = -5
print(sq.square())
print(sq.perimeter()) 

sq.size = 20
print(sq.size)
