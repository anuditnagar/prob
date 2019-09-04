import csv
from pprint import pprint

data = []

with open('BAJFINANCE-EQ.csv') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    for row in reader:
        # open high low close
        dat = [float(row[1]), float(row[2]), float(row[3]), float(row[4])]
        data.append(dat)

STARTAMOUNT = 10000
ANALYSECNT = 10
BETAMOUNT = 50

for ind in range(ANALYSECNT, len(data)):

    up, down, bet, result   = 0, 0, 0, 0
    for i in range(ind-ANALYSECNT, ind-1):
        if data[i][3] < data[i][3]:
            up+=1
        else:
            down+=1

    if(up >= down):
        # bet on up
        bet = 0
    else:
        # bet on down
        bet = 1

    result = 0
    if (data[ind][3] > data[ind-1][3]):
        # market went down
        result = 0
    else:
        # market went up
        result = 1

    if(result!=bet):
        STARTAMOUNT -= BETAMOUNT
    else:
        STARTAMOUNT -= BETAMOUNT

print(STARTAMOUNT)
