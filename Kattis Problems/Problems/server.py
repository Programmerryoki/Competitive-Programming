n,T = [int(i) for i in input().split()]
tasks = [int(i) for i in input().split()]
t = 0
n = 0
for task in tasks:
    if t + task <= T:
        t += task
        n += 1
    else:
        print(n)
        break
else:
    print(n)