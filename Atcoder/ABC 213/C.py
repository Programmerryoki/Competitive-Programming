H,W,N = [int(i) for i in input().split()]
cards = [[int(i) for i in input().split()]+[j] for j in range(N)]
cards.sort()
# print(cards)
p = -1
j = 0
for i in range(len(cards)):
    if cards[i][0] == p:
        cards[i][0] = j
    else:
        p = cards[i][0]
        j += 1
        cards[i][0] = j
# print(cards)
cards.sort(key=lambda x: x[1])
# print(cards)
p = -1
j = 0
for i in range(len(cards)):
    if cards[i][1] == p:
        cards[i][1] = j
    else:
        p = cards[i][1]
        j += 1
        cards[i][1] = j
# print(cards)
cards.sort(key=lambda x: x[-1])
print("\n".join(" ".join(map(str,i[:-1])) for i in cards))