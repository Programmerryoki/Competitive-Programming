N = int(input())
fa = []
b = False
for n in range(1, N+1):
    if n <= N//n:
        fa.append(N // n)
    else:
        break
total = sum(fa) * 2
total -= int(N**0.5) * len(fa)
print(total)