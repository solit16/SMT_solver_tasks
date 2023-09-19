from z3 import *
import sys

s = Solver()
numbers = [int(x) for x in sys.stdin.read().split()]
d = []

for i in range(len(numbers) + 12):
    d.append(BitVec(f'num_{i}', 32))

for i, num in enumerate(numbers):
    s.add(num == LShR((1103515245 * d[i] + 12345), 16))
for x in range(1, len(numbers) + 12):
      s.add(d[x] == (1103515245 * d[x - 1] + 12345))
if s.check() == sat:
  for i in d[-11:-1]:
    print(s.model()[i].as_long()>>16)
