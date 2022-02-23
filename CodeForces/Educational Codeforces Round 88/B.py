t = int(input())
for _ in range(t):
    n,m,x,y = [int(i) for i in input().split()]
    tc = 0
    for _ in range(n):
        line = input()
        if x < y/2:
            tc += x * line.count(".")
        else:
            line = line.split("*")
            for i in line:
                tc += (len(i)//2) * y + x * (len(i)%2)
    print(tc)