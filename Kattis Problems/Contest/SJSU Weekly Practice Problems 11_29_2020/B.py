from collections import Counter
from math import factorial as ft
from functools import reduce

while True:
    try:
        line = input()
    except:
        break
    cl = Counter(line)
    print(ft(len(line)) // reduce(lambda x,y:x*y, [ft(i) for i in cl.values()]))