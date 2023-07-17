import unittest
from Matrix import *


class TestMatrix(unittest.TestCase):
    

    def setUp(self) -> None:
        self.test_matrix_1 = Matrix([7,8], [9,10], [11, 12])
        self.test_matrix_2 = Matrix([1,2,3], [4,5,6])
        self.test_matrix_3 = Matrix([6,8], [9,11], [11, 10])

    def test_mul(self):
        self.assertEqual(self.test_matrix_2 * self.test_matrix_1,  Matrix([58, 64], [139, 154]))

    # Будет равна, так как в классе мы в качестве равенства двух матриц опредили равенсво суммы их элементов, 
    # чтобы ответ Matrix([58, 64, 139, 154]) считался ошибкой, нужно переопределять __eq__
    def test_mul_2(self):
        self.assertTrue(self.test_matrix_2 * self.test_matrix_1 ==  Matrix([58, 64, 139, 154])) 


    def test_mul_3(self):
        self.assertFalse(self.test_matrix_1 * self.test_matrix_2 ==  Matrix([58, 64], [139, 154]))

    def test_sum_1(self):
        self.assertEqual(self.test_matrix_3 + self.test_matrix_1,  Matrix([13, 16], [18, 21], [22, 22]))

    def test_sum_error(self):
        with self.assertRaises(ValueError):
            self.test_matrix_2 + self.test_matrix_1

if __name__ ==  "__main__":
    unittest.main(verbosity=2)