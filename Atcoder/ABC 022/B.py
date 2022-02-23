N = int(input())
seen = set()
flower = 0
for _ in range(N):
    A = int(input())
    if A in seen:
        flower += 1
    seen.add(A)
print(flower)