from math import gcd

while True:
    digs = input()
    if digs == "0":
        break
    frac = digs[2:-3]
    print(frac)