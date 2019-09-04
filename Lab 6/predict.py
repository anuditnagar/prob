import csv
from pprint import pprint

data = []

with open('BAJFINANCE-EQ.csv') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    for row in reader:
        dat = [float(row[1]), float(row[2]), float(row[3]), float(row[4])]
        data.append(dat)

STARTAMOUNT = 10000

originalOpen = data[0][0]
originalHigh = data[0][1]
originalLow = data[0][2]
originalClose = data[0][3]

for ind in range(len(data)):

    '''
    Average of ( (average of high and low) and (average of open and close) )
    Input : 10000
    Output : 21850
    Profit : 11850
    '''
    # predictedClose = ((( originalHigh + originalLow ) / 2) + (( originalOpen + originalClose ) / 2))/2

    '''
    Average of ( average of high and low )
    Input : 10000
    Output : 23050
    Profit : 13050
    '''
    predictedClose = (( originalHigh + originalLow ) / 2)

    '''
    Average of ( average of open and close )
    Input : 10000
    Output : 22650
    Profit : 12650
    '''
    # predictedClose = ( originalOpen + originalClose ) / 2

    actualClose = data[ind][3]
    diffClose = (predictedClose - actualClose)

    if (predictedClose > actualClose):
        STARTAMOUNT += 50
    else:
        STARTAMOUNT -= 50

    originalOpen = data[ind][0]
    originalHigh = data[ind][1]
    originalLow = data[ind][2]
    originalClose = data[ind][3]

    # print ([diffClose])

print(STARTAMOUNT)
# pprint(data[0:10])
