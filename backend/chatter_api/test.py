import random

numbers = ["1", "2", "3", "4", "5", "6"]
r = "".join(random.choices(numbers, k=6))
print(r)