# 📌Создайте класс студента. 
# ○Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. 
# ○Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы. 
# ○Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). 
# ○Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv


class Fullname:
    def __init__(self):
        self

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        
            self.validate(value)
            setattr(instance, self.param_name, value)

    
        

    def __delete__(self, instance):
        raise AttributeError(f"Свойство '{self.param_name}' нельзя удалить")
    
    def validate(self, value):
        if value.isalpha():
            if not value == value.lower().capitalize():
                raise ValueError(f"Значение {value} должно начинастя с заглавной буквы, а остальные символы должны быть строчными")

        else:
            raise ValueError(f"Значение {value} должно содерджать только буквы")
 
class Mark:
    
    def __init__(self,minimum_mark,maximum_mark ):
        self.minimum_mark = minimum_mark
        self.maximum_mark = maximum_mark

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        
            self.validate(value)
            setattr(instance, self.param_name, value)

    
        

    def __delete__(self, instance):
        raise AttributeError(f"Свойство '{self.param_name}' нельзя удалить")
    
    def validate(self, value):
        if not isinstance(value, int):
            
            raise ValueError(f"Значение {value} должно начинастя с заглавной буквы, а остальные символы должны быть строчными")
        if value < 2:
            self.value = 2 # Или лучше None вернуть
        if value >  5:
            self.value = 5 # Или лучше None вернуть

class Score:
    def __init__(self,minimum_mark,maximum_mark ):
        self.minimum_mark = minimum_mark
        self.maximum_mark = maximum_mark

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        
            self.validate(value)
            setattr(instance, self.param_name, value)

    
        

    def __delete__(self, instance):
        raise AttributeError(f"Свойство '{self.param_name}' нельзя удалить")
    
    def validate(self, value):
        if not isinstance(value, int):
            
            raise ValueError(f"Значение {value} должно начинастя с заглавной буквы, а остальные символы должны быть строчными")
        if value < 0:
            self.value = 0 # Или лучше None вернуть
        if value >  100:
            self.value = 100 # Или лучше None вернуть

    

class Student:
    first_name = Fullname()
    second_name = Fullname()
    last_name = Fullname()
    _mark = Mark(2,5)
    _score = Score(0,100)
    _subjects = []
    _subject_score= {}
    _subject_mark = [] # Для целей задачи, похоже, не важно соотнесение полученной оценки с предметом
   


    def __init__(self):
        self
        # self.first_name = first_name
        # self.second_name = second_name
        # self.last_name = last_name
        

        # self._subject_score = {}
        # self._subject_mark = []
    
    @property
    def mark(self):
        return self._mark
    
    @property
    def score(self):
        return self._score
    
    @mark.setter
    def mark(self, value):
        if 2 <= value < 6:
            self._subject_mark.append(value)
        else:
            raise ValueError(f"Проставляемая оценка выходит за диапозон используемой  школой шкалы оценивания") 
        
    @score.setter
    def score(self, subject, score):
        if 0 <= score < 101:
            self._subject_score[subject] = score
        else:
            raise ValueError("Итоговый результат должен быть в диапозоне от 0 до 100 баллов")
    
    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.last_name}"
    
    def __enter__(self):
        new_file = open("students_data.csv", "r", encoding="utf-8", newline="")
        csv_file = csv.reader(new_file)
        new_dict = {}
        for line in csv_file:
            key = f"{line[0]} {line[1]} {line[2]}"
            new_dict[key].append(line[3])
        return new_dict
    
    def __exit__(self,new_file, exc_type, exc_val, exc_tb):
        
        new_file.close()



stt_one  = Student()

with stt_one as st:
    print(st)




