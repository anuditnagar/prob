import csv
from pprint import pprint
from tabulate import tabulate

data = []

file_names = [
    'BAJFINANCE-EQ.csv',
    'BANKBARODA-EQ.csv',
    'PNB-EQ.csv',
    'YESBANK-EQ.csv'
]

BETAMOUNT = 50
calcs = []
phead=['Stock Name', 'Start Balance', 'Close Balance','Profit',  'Winning Bets', 'Win %',  'Loosing Bets', 'Loss %']
alpha  = 1;
for name in file_names:

    with open(name) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for row in reader:
            dat = [float(row[1]), float(row[2]), float(row[3]), float(row[4])]
            data.append(dat)

    STARTAMOUNT = 10000

    previousOpen = data[0][0]
    previouslHigh = data[0][1]
    previousLow = data[0][2]
    previousClose = data[0][3]

    wins = 0
    loss = 0

    for ind in range(1, len(data)):
        predictedMidline = (( previouslHigh + previousLow ) / 2)
        actualMidline = (( data[ind][0] + data[ind][3] ) / 2)

        if (data[ind][0] > data[ind][3]):
            # down
            if (predictedMidline < actualMidline):
                # low
                STARTAMOUNT += BETAMOUNT
                wins += 1
            else:
                # high
                STARTAMOUNT -= BETAMOUNT
                loss += 1
        elif (data[ind][0] < data[ind][3]):
            # up
            if (predictedMidline < actualMidline):
                # low
                STARTAMOUNT -= BETAMOUNT
                loss += 1
            else:
                # high
                STARTAMOUNT += BETAMOUNT
                wins += 1

        previousOpen = data[ind][0]
        previouslHigh = data[ind][1]
        previousLow = data[ind][2]
        previousClose = data[ind][3]

    calcs.append([name, 10000, STARTAMOUNT, STARTAMOUNT - 10000, wins, (wins/(wins+loss))*100, loss, (loss/(wins+loss))*100])

print(tabulate(calcs, headers=phead))
