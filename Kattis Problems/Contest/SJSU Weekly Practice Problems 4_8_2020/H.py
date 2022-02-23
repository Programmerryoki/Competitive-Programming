import bisect

seq = []
n,m,a,c,x = [int(i) for i in input().split()]
for i in range(n):
    x = (a*x + c) % m
    seq.append(x)
# print(seq)

def binary_search(arr, target):
    l = -1
    r = len(arr)
    while l < r:
        # print(l,r)
        m = max(0, (l + r)//2)
        if arr[m] == target:
            return True
        if arr[m] < target:
            if l == m:
                break
            l = m
        else:
            if r == m:
                break
            r = m
    return False

C = 0
for k in set(seq):
    # print(k)
    if binary_search(seq, k):
        # print(True)
        C += 1
print(C)