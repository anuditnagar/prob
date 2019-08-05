import random
from pprint import pprint

SAMPLE_SIZE = 5001

sample_data = [random.randint(1,6) for _ in range(SAMPLE_SIZE)]
sample_space = [[], [], [], [], [], []]

for index in range(0, len(sample_data)-1):
    sample_space[sample_data[index]-1].append(sample_data[index+1])

sample_space_count = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
for sample_index in range(0, 6):
    for element in sample_space[sample_index]:
        sample_space_count[sample_index][element-1]+=1

sample_space_prob = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
for sample_index in range(0, 6):
    element_count = len(sample_space[sample_index])
    for sampled_number in range(1, 7):
        sample_space_prob[sample_index][sampled_number-1] = float( sample_space_count[sample_index][sampled_number-1] / element_count)

# print("##### SAMPLE SPACE #####")
# pprint(sample_space)
print("\n")
print("##### SAMPLE SPACE COUNTS #####")
pprint(sample_space_count)
print("\n")
print("##### SAMPLE SPACE PROB #####")
pprint(sample_space_prob)
