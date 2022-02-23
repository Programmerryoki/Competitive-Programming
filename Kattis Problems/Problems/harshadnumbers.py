n = int(input())
found = False
while not found:
    digit = sum([int(i) for i in str(n)])
    if n%digit == 0:
        found = True
        print(n)
    n += 1