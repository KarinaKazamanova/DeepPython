import pytest

from Matrix import *

@pytest.fixture
def fix():
    return Matrix([7,8], [9,10], [11, 12])


def test_1(fix):
    assert fix.transponse() == Matrix([7, 9, 11], [8, 10, 12]) #Нужно переопределить метод __eq__, чтобы тест логичнее был

def test_2(fix):
    with pytest.raises(ValueError):
        fix * Matrix([1, 3]) 

def test_3(fix):
    with pytest.raises(ValueError):
        fix + Matrix([1, 3])   

def test_4(fix):
    assert fix + Matrix([1, 1], [0, 0], [3,6])  == Matrix([8, 9], [9, 10], [14, 18]) #Нужно переопределить метод __eq__, чтобы тест логичнее был
     
if __name__ == "__main__":
    pytest.main(["-v"])