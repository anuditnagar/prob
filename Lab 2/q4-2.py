from pprint import pprint
import re
import csv
from tqdm import tqdm

def writeTable(wordset, path ="ngram-3.csv", headers=["Word","Frequency"]):
    print("Storing")
    with open(path, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
        writer.writerow(headers)
        for line in tqdm(wordset) :
            try:
                writer.writerow (line)
            except:
                continue

def freq(wordset):
    freqTable = [];
    uniqueWordList = [];
    print("Indexing")
    for word in tqdm(wordset) :
        if (word not in uniqueWordList):
            freqTable.append([word, wordset.count(word)])
            uniqueWordList.append(word)
    writeTable(freqTable)

freqTable = []

with open('n-3.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    next(reader, None)
    for row in tqdm(reader):
        freqTable.append(str(row[0]).encode("UTF-8"))

freq(freqTable)
