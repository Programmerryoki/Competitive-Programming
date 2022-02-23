N,L = map(int, input().split())
K = int(input())
A = [int(i) for i in input().split()]+[L]

def pos(score):
    i = 0
    count = 0
    cur = 0
    while i < len(A) and count < K+1:
        # print(A[i], cur)
        if A[i] - cur >= score:
            count += 1
            cur = A[i]
        i += 1
    return count == K+1

low = 0
high = L
for i in range(50):
    mid = (low + high) // 2
    # print(mid, pos(mid))
    if pos(mid):
        low = mid
    else:
        high = mid
# print(low, high)
print(low)