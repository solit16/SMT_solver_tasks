from z3 import *
import sys

def dist_squared(xstart, ystart, xfin, yfin):
    return (xstart - xfin) * (xstart - xfin) + (ystart - yfin) * (ystart - yfin)

d1, d2, d3, e, x1, y1, x2, y2, x3, y3 = [int(x) for x in sys.stdin.read().split()]

s = Solver()

px, py = Reals('px py')

if d1 - e < 0: new1 = 0
else: new1 = d1 - e

if d2 - e < 0: new2 = 0
else: new2 = d2 - e

if d3 - e < 0: new3 = 0
else: new3 = d3 - e

s.add(dist_squared(x1, y1, px, py) >= new1**2)
s.add(dist_squared(x1, y1, px, py) <= (d1 + e)**2)

s.add(dist_squared(x2, y2, px, py) >= new2**2)
s.add(dist_squared(x2, y2, px, py) <= (d2 + e)**2)

s.add(dist_squared(x3, y3, px, py) >= new3**2)
s.add(dist_squared(x3, y3, px, py) <= (d3 + e)**2)

if s.check() == sat:
    print('YES')
else:
    print('NO')
