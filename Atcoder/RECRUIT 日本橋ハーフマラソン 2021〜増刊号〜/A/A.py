from sys import stdin
from time import time
input = stdin.readline

N,M,T = [int(i) for i in input().split()]
vegeday = [[[],[]] for i in range(T+1)]
veges = {}
for id in range(M):
    R,C,S,E,V = [int(i) for i in input().split()]
    vegeday[S][1].append((R,C))
    vegeday[E][0].append((R,C))
    veges[id] = (R,C,S,E,V)
start = time()
