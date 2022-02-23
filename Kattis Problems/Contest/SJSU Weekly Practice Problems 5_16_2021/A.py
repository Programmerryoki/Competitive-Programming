N = int(input())
M = int(input())
ans = ["*"*((M // N) + (i < M % N)) for i in range(N)]
print("\n".join(ans))