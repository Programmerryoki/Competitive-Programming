N = int(input())
sm = lambda x: ((x+1)*x) // 2
total = 0
for _ in range(N):
    A,B = map(int, input().split())
    total += sm(B) - sm(A-1)
print(total)