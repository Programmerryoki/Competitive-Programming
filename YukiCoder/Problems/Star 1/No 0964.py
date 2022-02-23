N = int(input())
ans = [str(i) * N for i in range(1,min(N+1, 10))]
if N == 10:
    ans += "0"*10
print("".join(ans))