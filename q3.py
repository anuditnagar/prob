from pprint import pprint
LINECOUNT = 119026

with open("lab-test.csv",encoding="utf8") as fp:
    r = enumerate(fp)
    for i, line in r:
        st = line.split("\"")
        pprint(st)
