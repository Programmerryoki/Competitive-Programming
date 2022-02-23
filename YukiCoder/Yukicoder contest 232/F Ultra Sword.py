N = int(input())
A = [int(i) for i in input().split()]
for a in A:
    print(bin(a))
    # print("20%d".format(bin(a)))
p = A[0]
for a in range(1,len(A)):
    b = A[a]
    if b > p:
        p, b = b, p
    while p % b != 0:
        # print(p,b)
        p %= b
        p, b = b, p%b
        # print(p,b)
    p = b
    # print(p)

print(p)
print(bin(p))
print(sum([i//p for i in A]))