class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) \
               + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'сумма клеток ' + str(self.nums + other.nums)


    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'вычитание не возможно'

    def __mul__(self, other):
        return 'умножение клеток ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'деление клеток ' + str(round(self.nums / other.nums))

#
cell_1 = Cell(22)
cell_2 = Cell(24)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(6))