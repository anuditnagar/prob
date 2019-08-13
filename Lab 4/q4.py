TOTAL_TOSSES = 100
TOTAL_CASES = 2 ** TOTAL_TOSSES

print("====Q1====")
print(2**70 / TOTAL_CASES)
print("====Q2====")
probSum = float(0)
for i in range(36, 101):
    prob = float((2**i) / TOTAL_CASES)
    print(prob)
    probSum = probSum + prob
    print(probSum)

# print(probSum)
