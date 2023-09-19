from z3 import *
import sys

s = Solver()

x = Real('x')

a, b, c, d, S = [int(x) for x in sys.stdin.read().split()]

s.add(x > 0)

s.add(x**2 * (a*d + b*c) == 2 * S * b * d)

if s.check() == sat:
	print(int(s.model()[x].as_decimal(100).split('.')[0]) + 1)
