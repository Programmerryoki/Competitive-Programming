N,K = [int(i) for i in input().split()]
total = []
for _ in range(N):
    A,B = [int(i) for i in input().split()]
    total.append(B)
    total.append(A-B)
total.sort(reverse=True)
print(sum(total[:K]))