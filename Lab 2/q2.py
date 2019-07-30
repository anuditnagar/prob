import random
from pprint import pprint

SAMPLE_SIZE = 51

sample_data = [random.randint(1,6) for _ in range(SAMPLE_SIZE)]
sample_space = [[], [], [], [], [], []]

for index in range(0, len(sample_data)-1):
    sample_space[sample_data[index]-1].append(sample_data[index+1])

pprint(sample_space)
