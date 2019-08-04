from pprint import pprint
import re
from tqdm import tqdm

with open("lab.csv",encoding="utf8") as fp:
    r = enumerate(fp)
    res = open("lab-q4.txt", "a")
    for i, line in tqdm(r):
        words = line.split(" ")
        for ind in range(0, len(words)):
            fr = words[ind].find("?")
            if(fr != -1):
                try:
                    res.write(f"[{i}] { str(words[ind][0:fr]) }\n")
                except:
                    continue
    res.close()
