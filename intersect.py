import sys
from z3 import *

x1, y1, x2, y2, X1, Y1, X2, Y2 = [int(x) for x in sys.stdin.read().split()]

s = Solver()

num1, num2 = Reals('num1 num2')
s.add(num1 >= 0)
s.add(num1 <= 1)
s.add(num2 >= 0)
s.add(num2 <= 1)

s.add(x1 + num1 * (x2 - x1) == X1 + num2 * (X2 - X1))
s.add(y1 + num1 * (y2 - y1) == Y1 + num2 * (Y2 - Y1))

if s.check() == sat:
    print('YES')
else:
    print('NO')
