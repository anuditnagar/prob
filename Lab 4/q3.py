import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

#
# @dev Load Up Data
#

freqTable = []
numbers = []
with open("numbers.txt") as fp:
    for i, line in enumerate(fp):
        numbers.append(int(line))

TOTAL_NUMBERS = len(numbers)

#
# @dev Calculate Probablities
#

for num in range(1,10):
    fr = numbers.count(num)
    freqTable.append((num, fr))

#
# @dev Plot Graph
#

dtype = [('Number', int), ('Frequency', int)]
npdata = np.array(freqTable, dtype=dtype)

sorted_data = np.sort(npdata, order='Frequency')[::-1]

pprint(sorted_data)
print("Plotting")

bar_labels = []
bar_heights = []
for names, values in sorted_data:
    bar_labels.append(str(names))
    bar_heights.append(values)

bar_x_positions  = [0,1,2,3,4, 5, 6, 7, 8]
plt.title('Histogram Plot')
plt.bar(bar_x_positions, bar_heights,  width = 1)
plt.xticks(bar_x_positions, bar_labels)
plt.show()
