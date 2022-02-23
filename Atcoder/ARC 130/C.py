A = input()
B = input()
diga = [0]*10
digb = [0]*10
for a in A:
    diga[int(a)] += 1
for b in B:
    digb[int(b)] += 1
for i in range(1,10):
    if diga[i] and digb[10-i]:
        diga[i] -= 1
        digb[10-i] -= 1
        break
offset = -1
total = 0
while sum(diga) and sum(digb):
    print(offset, diga, digb, total)
    for a in range(1,10):
        b = (10+offset - a) % 10
        d = min(diga[a], digb[b])
        if not d:
            continue
        diga[a], digb[b] = diga[a] - d, digb[b] - d
        total += ((a + b + offset) % 10) * d
    offset += 1
print(total)