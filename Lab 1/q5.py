from pprint import pprint
import re
import csv
from tqdm import tqdm

def writeTable(uniqueWordList, wordset, path ="lab-q5.csv", headers=["Word","Frequency"]):
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
    uniqueWordList = []
    print("Indexing")
    for word in tqdm(wordset) :
        if (word not in uniqueWordList):
            freqTable.append([word, wordset.count(word)])
            uniqueWordList.append(word)
    writeTable(uniqueWordList, freqTable)

with open("lab.csv",encoding="utf8") as fp:
    r = enumerate(fp)
    wordlist = []
    print("Cleaning")
    for i, line in tqdm(r):
        cleanLine = re.sub('\W+',' ', line)
        words = cleanLine.split(" ")
        for word in words:
            if(word != ''):
                wordlist.append(word.lower())
    freq(wordlist)
