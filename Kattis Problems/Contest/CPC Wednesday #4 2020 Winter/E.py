t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    prize = []
    for _ in range(n):
        # line = [int(i) for i in input().split()]
        # k, v = line[0], line[-1]
        # ti = line[1:-1]
        prize.append([int(i) for i in input().split()])
    prize.sort(key=lambda x: x[-1], reverse = True)
    ticket = [int(i) for i in input().split()]
    total = 0
    for a in prize:
        i = min([ticket[i-1] for i in a[1:-1]])
        total += i*a[-1]
        for b in a[1:-1]:
            ticket[b-1] -= i
    print(total)