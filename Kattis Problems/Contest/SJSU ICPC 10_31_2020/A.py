T = int(input())
for _ in range(T):
    n = int(input())
    card = []
    for i in range(n, 0, -1):
        card.insert(0,i)
        for j in [0]*i:
            # print(card)
            card = [card[-1]] + card[:-1]
    print(*card)