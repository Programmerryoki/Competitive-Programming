N, M = map(int, input().split())
wave = []
for _ in range(N):
    K, *A = [int(i) for i in input().split()]
    wave.append(set(A))

P,Q = map(int, input().split())
B = set([int(i) for i in input().split()])
total = 0
for index in range(N):
    if len(wave[index] & B) >= Q:
        total += 1
print(total)