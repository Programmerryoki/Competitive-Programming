k,n = [int(i) for i in input().split()]
W = [int(i) for i in input().split()]
SW = sum(W)
if SW % k != 0:
    print("NO")
else:
    ks = SW // k
    j = 0
    cur = 0
    count = 0
    for i in range(n):
        if cur + W[i] < ks:
            cur += W[i]
        elif cur + W[i] == ks:
            cur = 0
            count += 1
            j = i+1
        else:
            if count:
                print("NO")
                exit()
            while j < n and cur + W[i] > ks:
                cur -= W[j]
                j += 1
            cur += W[i]
            if cur == ks:
                count += 1
                cur = 0
                j = i+1
    if count >= k-1:
        print("YES")
    else:
        print("NO")