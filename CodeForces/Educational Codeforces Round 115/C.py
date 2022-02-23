t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    SA = sum(A)
    mean = SA / n
    total = 0
    count = {}
    for i in A:
        d = i-mean
        if -d in count:
            total += count[-d]
        if d not in count:
            count[d] = 0
        count[d] += 1
    # print(count)
    print(total)