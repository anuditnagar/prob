from pprint import pprint

with open("lab-test.csv",encoding="utf8") as fp:
    r = enumerate(fp)
    for i, line in r:
        st = line.split("\"")
        pprint(st)
