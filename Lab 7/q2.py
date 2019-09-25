import numpy as np
import math

SAMPLE_SIZE = 100000
a = 3
b = 5

# X ~ N(a, b2)
mu, sigma = a, b**2
X = np.random.normal(mu, sigma, SAMPLE_SIZE)

## (X-a)/b ~N(0,1).
newX  = [((num - a)/b) for num in X]
# print(X)
# print(newX)
print(f"Expected mu : {0}")
print(f"Calculated mu : {np.mean(newX)}")
print(f"Expected sigma : {math.floor(np.std(newX))}")
print(f"Calulated sigma : {np.std(newX)}")
