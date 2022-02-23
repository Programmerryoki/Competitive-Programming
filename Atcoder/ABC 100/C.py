N = int(input())
A = [int(i) for i in input().split()]
c = 0
for a in A:
    c += bin(a)[2:][::-1].index("1")
print(c)