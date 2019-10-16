import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

x = []
y = []

with open("dataset.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        x.append([round(float("0."+re.sub("\D","",x)[1:]), 2) for x in row[:10]])
        y.append(round(float("0."+re.sub("\D","",row[10])[1:]), 2))

print("[LAB8] Fitting Regression Model")
x = np.mat(x, dtype=float)
y = np.mat(y, dtype=float)
y = y.T
print(f"X : {x.shape}")
print(f"Y : {y.shape}")
print("[LAB8] Computing X*X.T")
x_x_trans = x.T * x
# print(x_x_trans)
print("[LAB8] Computing (X*X.T)^-1")
x_x_trans_inv = np.linalg.pinv(x_x_trans)
# print(x_x_trans_inv)
print("[LAB8] Computing ((X*X.T)^-1) * X.T * Y")
theta_cap =  (x_x_trans_inv * x.T) * y
print("[LAB8] Output => Predicted θ")
theta_cap = theta_cap.T
print("[LAB8] Output => Predicting y")
y_cap = theta_cap * x.T
y_cap = y_cap.T
print("[LAB8] Computing MSE")
mse = np.square(np.subtract(y, y_cap)).mean()
print(mse)

xAxis  = [x for x in range(x.shape[0])]
plt.plot(xAxis, y, label='Original Value')
plt.plot(xAxis, y_cap, label='Predicted Value')
plt.xlabel('Xi')
plt.ylabel('Y')
plt.title('Fitted Linear Regression Model')
plt.legend()
plt.show()
