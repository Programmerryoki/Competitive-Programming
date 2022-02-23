from collections import deque
from math import ceil

T = int(input())
for case in range(T):
    N,M = map(int, input().split())
    classes = [[j]+[int(i) for i in input().split()] for j in range(N)]
    classes = [i[:-1]+[ceil(i[-1] / M)] for i in classes]
    classes.sort(key=lambda x: (x[1],x[2],x[3],x[0]))
    clearTime = [[int(i) for i in input().split()] for j in range(N)]

    minRoom = 0
    clearRoom = 0
    emptyRoom = set()
    classHappening = deque()
    for i,[J,A,B,S] in enumerate(classes):
        tmp = []
        for k in emptyRoom:
            j,b,s = k
            

        while classHappening and classHappening[0][2] <= A:
            j,a,b,s = classHappening.popleft()
            emptyRoom.add((j,b,s))

        classHappening.append(i)
