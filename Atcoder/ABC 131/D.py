N = int(input())
work = [[int(i) for i in input().split()] for _ in range(N)]
work.sort(key=lambda x: (x[1], -x[0]))
time = 0
for i in range(N):
    A,B = work[i]
    if B < A + time:
        print("No")
        exit()
    time += A
print("Yes")