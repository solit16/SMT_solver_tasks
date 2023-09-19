from z3 import *
from itertools import permutations as perms

values = {}


def to_any(number, base):
    if number == 0:
        return 0
    new_num = ''
    while number != 0:
        new_num = str(number % base) + new_num
        number //= base
    return int(new_num)


def get_valid_indexes(num_index):
    num_with_base_9 = to_any(num_index, 9)
    if len(str(num_with_base_9)) < 2:
        return 0, num_with_base_9
    return int(str(num_with_base_9)[0]), int(str(num_with_base_9)[1])


def get_row(row_index):
    res = []
    for el in values:
        if el[0] == row_index:
            res.append(el)
    return res


def get_col(col_index):
    res = []
    for el in values:
        if el[1] == col_index:
            res.append(el)
    return res


def get_square(square_index):
    if square_index == 0:
        return [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    elif square_index == 1:
        return [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]
    elif square_index == 2:
        return [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)]
    elif square_index == 3:
        return [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
    elif square_index == 4:
        return [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
    elif square_index == 5:
        return [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)]
    elif square_index == 6:
        return [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)]
    elif square_index == 7:
        return [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)]
    elif square_index == 8:
        return [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]


sudoku = input()
s = Solver()

for row in range(9):
    for col in range(9):
        values[(row, col)] = Int(f'num_{row}_{col}')

sudoku_list = []
for digit in sudoku:
    sudoku_list.append(int(digit))

for index, num in enumerate(sudoku_list):
    if num != 0:
        values[get_valid_indexes(index)] = num

# условия
for ceil in values:
    s.add(And(values[ceil] >= 1, values[ceil] <= 9))

for i in range(9):
    for pair in perms(get_row(i), 2):
        s.add(values[pair[0]] != values[pair[1]])

for i in range(9):
    for pair in perms(get_col(i), 2):
        s.add(values[pair[0]] != values[pair[1]])

for i in range(9):
    for pair in perms(get_square(i), 2):
        s.add(values[pair[0]] != values[pair[1]])

s.check()
m = s.model()

res = ''
for ceil in values:
    if type(values[ceil]) != int:
        res += str(m[values[ceil]])
    else:
        res += str(values[ceil])

print(res)
