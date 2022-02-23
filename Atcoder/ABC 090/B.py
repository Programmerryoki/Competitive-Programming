A,B = [int(i) for i in input().split()]
c = 0
for n in range(A,B+1):
    c += str(n) == str(n)[::-1]
print(c)