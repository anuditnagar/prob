import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
import re
import csv
from tqdm import tqdm

def freq(wordset):
    freqTable = [];
    uniqueWordList = []
    for word in tqdm(wordset, desc='Indexing') :
        if (word not in uniqueWordList):
            freqTable.append( (str(word),int(wordset.count(word))) )
            uniqueWordList.append(word)

    # pprint(freqTable)

    print("Sorting")

    dtype = [('word', '|S10'), ('frequency', int)]
    npdata = np.array(freqTable, dtype=dtype)
    sorted_data = np.sort(npdata, order=['frequency', 'word'])[::-1]
    required_data = sorted_data[0:5].tolist();

    print("Plotting")
    # print(required_data)
    bar_labels = []
    bar_heights = []
    for names, values in required_data:
        bar_labels.append(names.decode('UTF-8'))
        bar_heights.append(values)

    bar_x_positions  = [0,1,2,3,4]
    plt.bar(bar_x_positions, bar_heights,  width = .5)
    plt.xticks(bar_x_positions, bar_labels)
    plt.show()

with open("lab.csv",encoding="utf8") as fp:
    r = enumerate(fp)
    wordlist = []
    for i, line in tqdm(r, desc='Cleaning'):
        if (i<1000):
            cleanLine = re.sub('\W+',' ', line)
            words = cleanLine.split(" ")
            for word in words:
                if(word != ''):
                    wordlist.append(word.lower())
        else:
            break
    freq(wordlist)
