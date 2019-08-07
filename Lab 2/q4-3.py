import csv
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from pprint import pprint

print("Indexing")
freqTable = []
with open('ngram-4.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    next(reader, None)
    for row in tqdm(reader):
        freqTable.append((str(row[0]).encode("UTF-8"),int(row[1])))

csvFile.close()

dtype = [('Word', 'U40'), ('Frequency', int)]
npdata = np.array(freqTable[:], dtype=dtype)

sorted_data = np.sort(npdata, order=['Frequency', 'Word'])[::-1]
required_data = sorted_data[0:5].tolist();
pprint(required_data)

print("Plotting")
bar_labels = []
bar_heights = []
for names, values in required_data:
    bar_labels.append(str(names)[2:-1])
    bar_heights.append(values)

bar_x_positions  = [0,1,2,3,4]
plt.title('Top 5 used words')
plt.bar(bar_x_positions, bar_heights,  width = .5)
plt.xticks(bar_x_positions, bar_labels)
plt.show()
