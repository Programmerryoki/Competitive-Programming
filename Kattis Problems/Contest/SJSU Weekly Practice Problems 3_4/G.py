N = int(input())
lo = 0
pile = []
for a in range(N):
    n = input()
    if n == "O":
        lo = a
    pile.append(n)

n = pile.count("O")
c = 0
while n > 0:
    pile[lo] = "Z"
    n -= 1
    c += 1
    ori = lo
    for a in range(lo+1, N):
        if pile[a] == "Z":
            pile[a] = "O"
            lo = a
            n += 1
    try:
        lo = len(pile) - pile[::-1].index("O") - 1
    except:
        break
print(c)