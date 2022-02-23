T = int(input())
for a in range(T):
    days = [int(i) for i in input().split()[:-1]]
    impo = 0
    for b in range(1, len(days)):
        if days[b] > days[b-1] * 2:
            impo += days[b] - days[b-1] * 2
    print(impo)