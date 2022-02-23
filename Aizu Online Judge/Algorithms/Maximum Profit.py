import sys
readlines = sys.stdin.buffer
n = int(input())
mi = 10**9
mv = -10**9
for N in map(int, readlines):
    # print(N)
    # N = int(input())
    if N - mi > mv:
        mv = N - mi
    if N < mi:
        mi = N
print(mv)