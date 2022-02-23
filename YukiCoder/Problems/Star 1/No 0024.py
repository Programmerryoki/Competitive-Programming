N = int(input())
ans = {str(i) for i in range(10)}
for _ in range(N):
    A,B,C,D,R = input().split()
    remove = set([A,B,C,D])
    if R == "NO":
        ans -= remove
    else:
        ans &= remove
print(ans.pop())