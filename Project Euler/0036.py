s = []
pal = lambda x: x == x[::-1]
for n in range(1,10**6):
    if pal(str(n)) and pal(bin(n)[2:]):
        s.append(n)
        print(n)
print(sum(s))