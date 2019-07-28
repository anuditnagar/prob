from pprint import pprint
import re

with open("lab-test.csv",encoding="utf8") as fp:
    r = enumerate(fp)
    for i, line in r:
        words = line.split(" ")
        for ind in range(0, len(words)):
            fr = words[ind].find("?")
            if(fr != -1):
                print(f"[{i}] { words[ind][0:fr] }")
