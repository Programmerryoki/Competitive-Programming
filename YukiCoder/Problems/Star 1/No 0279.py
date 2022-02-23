from collections import Counter
S = Counter(input())
c = 0
try:
    S["t"],S["r"],S["e"]
    print(min(S["t"], S["r"], S["e"]//2))
except:
    print(0)