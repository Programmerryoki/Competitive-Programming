dt = set()
lim = 100
for a in range(2,lim+1):
    for b in range(2,lim+1):
        dt.add(a**b)
print(len(dt))