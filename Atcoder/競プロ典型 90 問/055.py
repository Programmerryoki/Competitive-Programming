N,P,Q = [int(i) for i in input().split()]
A = [int(i) % P for i in input().split()]
count = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            for l in range(k+1, N):
                for m in range(l+1, N):
                    num = ((((((A[i]*A[j])%P)*A[k])%P)*A[l])%P*A[m])%P
                    if num == Q:
                        count += 1
print(count)