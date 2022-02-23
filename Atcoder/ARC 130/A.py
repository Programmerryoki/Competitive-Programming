N = int(input())
S = input() + " "
j = 0
total = 0
pv = ""
for i in range(len(S)):
    if S[i] == pv:
        continue
    d = i - j + 1
    total += d*(d-1)//2
    j = i + 1
    pv = S[i]
print(total)