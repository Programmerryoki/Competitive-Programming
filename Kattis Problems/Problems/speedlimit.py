n = int(input())
while n != -1:
    total = 0
    pt = 0
    for a in range(n):
        m = input().split(" ")
        sp = int(m[0])
        t = int(m[1])
        total += sp * (t-pt)
        pt = t
    print(total,"miles")
    n = int(input())