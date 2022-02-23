H, W, A, B = [int(i) for i in input().split()]
comb = [1]*(H-B) + [0]*B
for a in range(W-1):
    temp = [i for i in comb]
    # print(temp)
    if a < A:
        for b in range(1, H - B):
            comb[b] = temp[b] + comb[b-1]
    elif a == A:
        for b in range(H-B, len(comb)):
            comb[b] = 1
        for b in range(1, len(comb)):
            comb[b] = temp[b] + comb[b-1]
    else:
        for b in range(1, len(comb)):
            comb[b] = temp[b] + comb[b-1]
# print(comb)
print(comb[-1])