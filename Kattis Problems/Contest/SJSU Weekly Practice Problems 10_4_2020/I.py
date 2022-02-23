S = input()
E = int(input())
rhymes = []

for ajod in range(E):
    temp = input().split()
    val = False
    for i in temp:
        if i in S and S[::-1].index(i[::-1]) == 0:
            val = True
            break
    if val:
        rhymes.extend(temp)

P = int(input())
for _ in range(P):
    inp = input()
    yes = False
    for rhyme in rhymes:
        if rhyme in inp and inp[::-1].index(rhyme[::-1]) == 0:
            yes = True
            break
    if yes:
        print("YES")
    else:
        print("NO")