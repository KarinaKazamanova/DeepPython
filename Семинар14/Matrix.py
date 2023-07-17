import doctest

class Matrix():
    """
    >>> Matrix([1,2], [2,3,5], [4]) == ValueError
    Traceback (most recent call last):
        ...
    ValueError

    >>> Matrix([1,2,3], [4,5,6]) * Matrix([7,8], [9,10], [11, 12]) == Matrix([58, 64], [139, 154])
    True

    >>> Matrix([1,2,3], [4,5,6]).transponse() == Matrix([1,4], [2,5], [3, 6])
    True
    
    """
    res_matrix = []

    def __init__(self, *args):
        if max(args, key=len) == min(args, key=len):
            self.res_matrix = [arg for arg in args]
        else:
            raise ValueError

    def __str__(self):
        res_string = ''
        max_= 0
        for line in self.res_matrix:
            for i in line:
                if len(str(i)) > max_:
                    max_ = len(str(i))
        
        for i in self.res_matrix:
            for j in i:
                res_string += (f" {j:>{max_}}")
            res_string += "\n"
        return res_string
    
    def __repr__(self) -> str:
        string_ = ""
        for i, line in enumerate(self.res_matrix, 1):
            string_+= f" {i} - {line}"
        return string_
            
    def __eq__(self, other):
        sum_1 = 0
        for line in self.res_matrix:
            sum_1 += sum(line)
        sum_2 = 0
        for line in other.res_matrix:
            sum_2 += sum(line)
        return sum_1 == sum_2
    

    def __add__(self, other):
        if len(self.res_matrix) == len(other.res_matrix) and len(self.res_matrix[0]) == len(other.res_matrix[0]):
            new_matrix = []
            for i in range(len(self.res_matrix)): 
                new_matrix.append(list(map(sum, zip(self.res_matrix[i],other.res_matrix[i]))))
            return Matrix(*new_matrix)
        else:
            raise ValueError
        
    def transponse(self):
        new_matrix = [[0 for _ in range(len(self.res_matrix))] for _ in range(len(self.res_matrix[0]))]
        for i in range(len(self.res_matrix)):
            for j in range(len(self.res_matrix[i])):
                new_matrix[j][i] = self.res_matrix[i][j]
          
        return Matrix(*new_matrix)
    
    def __mul__(self, other):
        new_other_matrix = other.transponse()
        new_res_matrix = []
        if len(self.res_matrix) == len(new_other_matrix.res_matrix) and len(self.res_matrix[0]) == len(new_other_matrix.res_matrix[0]):
            for i in range(len(self.res_matrix)):
                raw = []
                for j in range(len(self.res_matrix)):
                    number  = sum([l for l in map(lambda x, y: x * y, self.res_matrix[i], new_other_matrix.res_matrix[j])])
                    raw.append(number)
                new_res_matrix.append(raw)
            return Matrix(*new_res_matrix)
        else:
            raise ValueError

if __name__ == "__main__":
    n_m_1 = Matrix([1,2,3], [4,5,6])
    # print(n_m_1.__repr__)
    n_m_2 = Matrix([7,8], [9,10], [11, 12])
    print(n_m_2 * n_m_1)
    # print(n_m_1.transponse())
    # doctest.testmod(verbose=True)
