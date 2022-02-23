P = int(input())
for _ in range(P):
    K, t = input().split()
    K = int(K)
    p,q = [int(i) for i in t.split("/")]
    n = ""
    while p != 1 or q != 1:
        if p > q:
            n += "1"
            p,q = p - q, q
        else:
            n += "0"
            p,q = p, q - p
    print(K,int((n+"1")[::-1], 2))