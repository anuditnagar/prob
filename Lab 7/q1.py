import numpy as np

SAMPLE_SIZE = 100000

# X ~ N(0,1)
mu, sigma = 0, 1
X = np.random.normal(mu, sigma, SAMPLE_SIZE)

a = 3
b = 5

# aX+b ~ N(b,a2)
newX  = [(a*num)+b for num in X]

print(f"Expected mu : {b}")
print(f"Calculated mu : {np.mean(newX)}")
print(f"Expected sigma : {a}")
print(f"Calulated sigma : {np.std(newX)}")
