import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
import csv

df = pd.read_csv('dataset.csv')
corrMatrix = df.corr()
print(corrMatrix)
plt.matshow(corrMatrix)
plt.show()

x = []
y = []

with open("dataset.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        x.append([round(float("0."+re.sub("\D","",x)[1:]), 2) for x in row[:10]])
        y.append(round(float("0."+re.sub("\D","",row[10])[1:]), 2))

plt.plot(x)
plt.show()
