from collections import Counter
from math import factorial
n = int(input())
s = list(input())
print(len(s),"C",3,"=",factorial(len(s))/(factorial(3)*factorial(len(s)-3)))
print(Counter(s).values())
c = 0
for a in Counter(s).values():
    c += factorial(a-1)
print(c)