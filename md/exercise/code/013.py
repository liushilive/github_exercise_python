from functools import reduce

for n in range(100, 1000):
    if reduce(lambda x, y: x+y, map(lambda z: int(z) ** 3, str(n))) == n:
        print(n)
