n = int(input())
S = input()
T = input()
c = 0
for i in range(n):
    c += S[i] != T[i]
print(c)