import matplotlib.pyplot as plt
import numpy as np

SAMPLE_SIZE = 10000

# normal dist
mu, sigma = 3, 5**2
norm = np.random.normal(mu, sigma, SAMPLE_SIZE)
plt.hist(norm)
plt.show()

# poisson dist
norm = np.random.poisson(5, SAMPLE_SIZE)
count, bins, ignored = plt.hist(norm, 15, normed=True)
plt.show()

# Exp dist
exp = np.random.exponential(100, SAMPLE_SIZE)
plt.hist(exp)
plt.show()
