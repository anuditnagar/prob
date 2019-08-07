from pprint import pprint
import re
import csv
from tqdm import tqdm

def writeSingle(table, path ="n-x.csv", headers=["Word"]):
    print("Storing")
    with open(path, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
        writer.writerow(headers)
        for row in tqdm(table) :
            try:
                writer.writerow (row)
            except:
                continue

with open("lab.csv",encoding="utf8") as fp:
    r = enumerate(fp)
    ngrams_2 = []
    ngrams_3 = []
    ngrams_4 = []
    print("Cleaning")
    for i, line in tqdm(r):
        cleanLine = re.sub('\W+',' ', line).lstrip(' ')
        for N in range(2, 5):
            spCnt = 0
            previousInd = 0
            for ind in range(len(cleanLine)):
                if(cleanLine[ind] == " "):
                    spCnt+=1
                    if(spCnt == N):
                        eval(f"ngrams_{N}.append([cleanLine[previousInd:ind]])")
                        spCnt = 0
                        previousInd = ind+1
                        ind+=1

    writeSingle(ngrams_2, path="n-2.csv")
    writeSingle(ngrams_3, path="n-3.csv")
    writeSingle(ngrams_4, path="n-4.csv")
