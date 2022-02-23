t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    A.sort()
    i = -1
    c = 0
    for a in A:
        if a%k == 0:
            continue
        if i >= a%k:
            c += k - i + a%k
            i = 0
        else:
            c += a%k - i
            i = a%k
    print(c)

# t = int(input())
# for _ in range(t):
#     n,k = [int(i) for i in input().split()]
#     a = [int(i) for i in input().split()]
#     mod = [0]*k
#     for i in a:
#         mod[i%k] += 1
#     mod = mod[1:] if len(mod[1:]) != 0 else [0]
#     m = max(mod)
#     print(m*k - mod.index(m))