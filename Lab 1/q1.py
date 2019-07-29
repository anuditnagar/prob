LINECOUNT = 119026

with open("lab.csv",encoding="utf8") as fp:
    r = enumerate(fp)
    for i, line in r:
        if i in range(0,20) or i in range(LINECOUNT-20, LINECOUNT):
            print(f"[{i}] {line}")
