import sys
from z3 import *


def dist_squared(xstart, ystart, xfin, yfin):
    return (xstart - xfin) * (xstart - xfin) + (ystart - yfin) * (ystart - yfin)


s = Solver()

x_first, y_first, x_second, y_second = Reals('x_first y_first x_second y_second')
t = Real('t')

s.add(t >= 0)

x1, y1, x2, y2, v, X1, Y1, X2, Y2, V, d = [int(q) for q in sys.stdin.read().split()]

# x1, y1, x2, y2, v, X1, Y1, X2, Y2, V, d = Reals('x1 y1 x2 y2 v X1 Y1 X2 Y2 V d')

# k1 = (y1 - y2) / (x1 - x2)
# k2 = (Y1 - Y2) / (X1 - X2)
#
# b1 = y1 - x1 * ((y1 - y2) / (x1 - x2))
# b2 = Y1 - X1 * ((Y1 - Y2) / (X1 - X2))

s.add(dist_squared(x_first, y_first, x_second, y_second) <= d * d)

s.add((x_first - x1) ** 2 + (y_first - y1) ** 2 == v * t * v * t)
s.add((x_second - X1) ** 2 + (y_second - Y1) ** 2 == V * t * V * t)
s.add((y_first - y1) * (x2 - x1) == (x_first - x1) * (y2 - y1))
s.add((y_second - Y1) * (X2 - X1) == (x_second - X1) * (Y2 - Y1))
if y2 > y1:
    s.add(y_first >= y1)
elif y2 == y1:
    if x2 > x1:
        s.add(x_first >= x1)
    else:
        s.add(x_first <= x1)
else:
    s.add(y_first <= y1)

if Y2 >= Y1:
    s.add(y_second >= Y1)
elif Y2 == Y1:
    if X2 > X1:
        s.add(x_second >= x1)
    else:
        s.add(x_second <= x1)
else:
    s.add(y_second <= Y1)
if s.check() == sat:
    print('YES')
else:
    print('NO')
