from pprint import pprint
from tabulate import tabulate

def getNumbers(filename = "numbers.txt"):
    arr = []
    with open(filename) as fp:
        for i, line in enumerate(fp):
            arr.append(int(line))
    return arr

numbers = getNumbers()
TOTAL_NUMBERS = len(numbers)
numFreq = []
for num in range(1,10):
    fr = numbers.count(num)
    cdf = 0
    for row in numFreq:
        cdf += row[2]
    pmf = float(fr/TOTAL_NUMBERS)
    numFreq.append([num, fr,pmf , cdf+pmf])

print(tabulate(numFreq, ["Number", "Frequency", "PMF", "CDF"],tablefmt="grid"))
