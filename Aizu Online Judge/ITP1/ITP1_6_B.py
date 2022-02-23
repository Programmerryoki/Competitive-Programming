cards = []
for a in range(1,14):
    cards += ["S "+str(a), "H "+str(a), "C "+str(a), "D "+str(a)]
n = int(input())
for a in range(n):
    cards.remove(input())
order = ["S","H","C","D"]
cards.sort(key = lambda x: order.index(x[0]))
if len(cards) != 0:
    print("\n".join(cards))