M = int(input())
digit = []
dig = [0 for i in range(10)]
for a in range(M):
    s = [int(i) for i in input().split()]
    digit.extend(str(s[0]) * s[1])
    dig[s[0]] += s[1]

print(digit)
c = 0

print(c)