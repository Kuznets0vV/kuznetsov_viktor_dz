class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        matrix_sum = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'ошибка'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                matrix_sum += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'ошибка'
        return matrix_sum
matrix_1 = Matrix([[6, 3], [3, 8], [3, 6], [7, 3]])
matrix_2 = Matrix([[2, 6], [5, 5], [6, 3], [11, 15]])

print(matrix_1 + matrix_2)
