N = int(input())
d = [int(input()) for _ in range(N)]
d = sorted(set(d), reverse=True)
print(len(d))