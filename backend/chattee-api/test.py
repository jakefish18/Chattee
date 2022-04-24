import random

numbers = tuple(map(str, range(1, 7)))
r = random.choices(numbers, k=6)
print(*r, sep='')
