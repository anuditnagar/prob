from math import factorial as fact
def nCr(n , r):
    if (r==0):
        return 1
    if (r==1):
        return n
    return float(fact(n) / (fact(r)*fact(n-r)))

TOTAL_TOSSES = 100
TOTAL_CASES = 2 ** TOTAL_TOSSES

print("====Q1====")
print(float(nCr(TOTAL_TOSSES, 30) * ((1/2)**TOTAL_TOSSES)))

print("====Q2====")
probSum = 1
for i in range(1, 36):
    probSum -= (nCr(TOTAL_TOSSES, i) * ((1/2)**TOTAL_TOSSES))
print(probSum)

print("====Q3====")
probSum = 1
for i in range(1, 60):
    probSum -= (nCr(TOTAL_TOSSES, i) * ((1/2)**TOTAL_TOSSES))
for i in range(70, TOTAL_TOSSES):
    probSum -= (nCr(TOTAL_TOSSES, i) * ((1/2)**TOTAL_TOSSES))

print(probSum)
