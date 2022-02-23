from collections import deque

N, M = [int(i) for i in input().split()]
time = [[int(i) for i in input().split()] for j in range(N)]
stage = [[0,0]*2 for i in range(N)]
prev = deque([0]*N)
for a in range(M):
    t = 0
