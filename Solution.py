# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import erf,sqrt

def cumulative(m,sd,x):
    return (1 + erf((x - m) / (sd * sqrt(2)))) / 2

print(1 - round(cumulative(70, 10, 80), 4)) * 100
print(1 - round(cumulative(70, 10, 60), 4)) * 100
print(round(cumulative(70, 10, 60), 4)) * 100
