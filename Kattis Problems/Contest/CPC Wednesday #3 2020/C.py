C = int(input())
for a in range(C):
    line = [int(i) for i in input().split()]
    N = line[0]
    line = line[1:]
    t = sum(line)/len(line)
    c = 0
    for n in line:
        if n > t:
            c += 1
    print("{0:.3f}%" .format(100*c/N))