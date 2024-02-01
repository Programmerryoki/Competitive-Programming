for a in range(1000):
    for b in range(a+1, 1000):
        c = 1000 - a - b
        if not a<b<c:
            break
        if a**2 + b**2 == c**2:
            print(a,b,c,a * b * c)