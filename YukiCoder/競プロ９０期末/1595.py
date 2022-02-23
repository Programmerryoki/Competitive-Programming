p,q,r,K = [int(i) for i in input().split()]
p%=10
q%=10
r%=10
arr = [p,q,r]
rep = {}
for i in range(4, K+1):
    t = sum(arr[-3:])
    t %= 10
    arr.append(t)
    tup = tuple(arr[-4:])
    if tup in rep:
        # print(tup)
        arr = arr[rep[tup]-4:-4]
        break
    rep[tup] = i
# print((K-1) % len(arr))
print(arr[(K-1) % len(arr)])
# print(arr)