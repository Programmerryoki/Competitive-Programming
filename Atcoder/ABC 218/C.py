N = int(input())
S = [list(input()) for i in range(N)]
T = [list(input()) for i in range(N)]

def reduce(arr):
    bv = -1
    ev = -1
    for i in range(len(arr)):
        if "#" in arr[i]:
            if bv == -1:
                bv = i
            ev = i
    bh = -1
    eh = -1
    for i in range(len(arr[0])):
        if "#" in [arr[k][i] for k in range(len(arr))]:
            if bh == -1:
                bh = i
            eh = i
    i = N-1
    while i >= 0:
        if (i < bv or ev < i) and arr[i].count(".") == N:
            arr.pop(i)
        i -= 1
    j = N-1
    while j >= 0:
        c = 0
        for i in range(len(arr)):
            if arr[i][j] == ".":
                c += 1
        if (j < bh or eh < j) and c == len(arr):
            for i in range(len(arr)):
                arr[i].pop(j)
        j -= 1
    return arr

def rotate(arr):
    ans = [[""]*len(arr) for i in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            ans[j][len(arr)-i-1] = arr[i][j]
    return ans

S = reduce(S)
T = reduce(T)
for r in range(4):
    if S == T:
        print("Yes")
        exit()
    S = rotate(S)
print("No")

# from collections import deque
#
# N = int(input())
# S = [input() for i in range(N)]
# T = [input() for i in range(N)]
# moves = [(-1,0),(0,1),(1,0),(0,-1)]
# rev = {0:2,2:0,1:3,3:1}
# sg = {}
# for i in range(N):
#     for j in range(N):
#         if S[i][j] == ".":
#             continue
#         for i,(dx,dy) in enumerate(moves):
#             x,y = dx+i,dy+j
#             if 0<=x<N and 0<=y<N and S[x][y] == "#":
#                 if (i,j) not in sg:
#                     sg[(i,j)] = {}
#                 if (x,y) not in sg:
#                     sg[(x,y)] = {}
#                 sg[(i,j)][i] = (x,y)
#                 sg[(x,y)][rev[i]] = (i,j)
# tg = {}
# for i in range(N):
#     for j in range(N):
#         if T[i][j] == ".":
#             continue
#         for i,(dx,dy) in enumerate(moves):
#             x,y = dx+i,dy+j
#             if 0<=x<N and 0<=y<N and T[x][y] == "#":
#                 if (i,j) not in tg:
#                     tg[(i,j)] = {}
#                 if (x,y) not in tg:
#                     tg[(x,y)] = {}
#                 tg[(i,j)][i] = (x,y)
#                 tg[(x,y)][rev[i]] = (i,j)
# print(sg.keys())
# print(tg.keys())
# for rotation in range(4):
#     for i in sg:
#         for j in tg:
#             sque = deque([i])
#             sseen = {i}
#             tque = deque([j])
#             while sque and tque:
#                 s = sque.popleft()
#                 t = tque.popleft()
#                 if set((i+rotation)%4 for i in sg[s]) != set(i for i in tg[t]):
#                     break
#                 for nxt in sg[s]:
#                     if sg[s][nxt] in sseen:
#                         continue
#                     sseen.add(sg[s][nxt])
#                     sque.append(sg[s][nxt])
#                     tque.append(tg[t][(nxt+rotation)%4])
#             else:
#                 continue
#             if not sque and not tque:
#                 print("Yes")
#                 exit()
# print("No")