N,K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
A.sort(reverse=True)
i = 1
while i < K:
    if sum(A[:i]) < sum(A[:i+1]):
        i += 1
    else:
        break
print(sum(A[:i]))