import numpy as np

print(10**5)

for _ in range(10 ** 5):
    print(np.random.choice(100) - 50, end=" ")

print()

for i in range(10 ** 5 - 1):
    print(i + 1, i + 2)
