A,B,K = [int(i) for i in input().split()]
ans = list(set([i for i in range(A,min(A+K, B+1))] + [j for j in range(max(A, B-K+1),B+1)]))
ans.sort()
print("\n".join(map(str, ans)))