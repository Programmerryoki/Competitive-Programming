L = int(input())
M = int(input())
N = int(input())
t = L*100 + M*25 + N
c = 0
t %= 1000
c += t//100
t %= 100
c += t//25
t %= 25
c += t
print(c)