from time import time
from random import shuffle, randint, seed
from sys import setrecursionlimit, stdin
setrecursionlimit(10**8)
seed(2000)

def main():
    input = stdin.readline

    dirs = "UDLR"
    dirmove = [(-1,0), (1,0), (0,-1), (0,1)]


    def getscore(t,p, si,sj,moves):
        score = p[si][sj]
        pos = [si, sj]
        seen = {t[si][sj]}
        for move in moves:
            dx,dy = dirmove[dirs.index(move)]
            x,y = pos[0]+dx, pos[1]+dy
            if 0 <= x < 50 and 0 <= y < 50:
                if t[x][y] in seen:
                    return 0
                seen.add(t[x][y])
                score += p[x][y]
                pos[0] = x
                pos[1] = y
            else:
                return 0
        return score


    SI,SJ = map(int, input().split())
    t = [[int(i) for i in input().split()] for j in range(50)]
    p = [[int(i) for i in input().split()] for j in range(50)]
    starttime = time()
    bmoves = []
    bs = 0
    seen = {t[SI][SJ]}
    options = [i for i in range(4)]
    def search(starts, si,sj,move,last):
        nonlocal options, bmoves, starttime, bs
        s = getscore(t,p,starts[0], starts[1],move)
        # print(s,move)
        if s > bs:
            bmoves = move.copy()
            bs = s
        if time() - starttime > 1.95:
            raise ConnectionError
        around = []
        if 0 < si:
            around.append((si-1,sj,0))
        if 0 < sj:
            around.append((si,sj-1,2))
        if si < 49:
            around.append((si+1,sj,1))
        if sj < 49:
            around.append((si,sj+1,3))
        around.sort(key=lambda T: -p[T[0]][T[1]])
        tmp = randint(0,50)
        if tmp == 10:
            shuffle(around)
        for i,j,I in around:
            x,y = i,j
            # print(i,j,I)
            if 0 <= x < 50 and 0 <= y < 50 and t[x][y] not in seen:
                seen.add(t[x][y])
                search(starts, x,y,move+[dirs[I]],I)
                seen.remove(t[x][y])

    si,sj = SI,SJ
    move = []
    last = -1
    try:
        search((SI,SJ), si, sj, move, last)
    except ConnectionError:
        pass
    print("".join(bmoves))

if __name__ == "__main__":
    main()

# with strong and redos
# from time import time
# from random import shuffle, randint
# from collections import deque
# from sys import setrecursionlimit
# setrecursionlimit(10**8)
#
# dirs = "UDLR"
# dirmove = [(-1,0), (1,0), (0,-1), (0,1)]
#
#
# def getscore(t,p, si,sj,moves):
#     score = p[si][sj]
#     pos = [si, sj]
#     seen = {t[si][sj]}
#     for move in moves:
#         dx,dy = dirmove[dirs.index(move)]
#         x,y = pos[0]+dx, pos[1]+dy
#         if 0 <= x < 50 and 0 <= y < 50:
#             if t[x][y] in seen:
#                 return 0
#             seen.add(t[x][y])
#             score += p[x][y]
#             pos[0] = x
#             pos[1] = y
#         else:
#             return 0
#     return score
#
#
# SI,SJ = map(int, input().split())
# t = [[int(i) for i in input().split()] for j in range(50)]
# p = [[int(i) for i in input().split()] for j in range(50)]
# starttime = time()
# bmoves = []
# bs = 0
# seen = {t[SI][SJ]}
# options = [i for i in range(4)]
# redos = deque()
# def search(starts, si,sj,move,last):
#     global options, bmoves, starttime, bs, redos
#     s = getscore(t,p,starts[0], starts[1],move)
#     # print(s,move)
#     if s > bs:
#         bmoves = move.copy()
#         bs = s
#     if time() - starttime > 1.95:
#         raise ConnectionError
#
#     # around = []
#     # if 0 < si:
#     #     around.append((t[si-1][sj], p[si-1][sj],1))
#     # if 0 < sj:
#     #     around.append((t[si][sj-1],p[si][sj-1],3))
#     # if si < 49:
#     #     around.append((t[si+1][sj],p[si+1][sj],0))
#     # if sj < 49:
#     #     around.append((t[si][sj+1],p[si][sj+1],2))
#     # repoint = t[si][sj] in [i[0] for i in around]
#     # if repoint:
#     #     redos.appendleft((si,sj,move,last))
#     # around.sort(key=lambda T: T[1])
#     # for T,P,I in around:
#     #     x,y = si+dirmove[I][0], sj+dirmove[I][1]
#     #     if 0 <= x < 50 and 0 <= y < 50 and t[x][y] not in seen:
#     #         seen.add(t[x][y])
#     #         search(starts, x,y,move+[dirs[I]],I)
#     #         seen.remove(t[x][y])
#
#     shuffle(options)
#     for i in options:
#         x,y = si+dirmove[i][0], sj+dirmove[i][1]
#         if 0 <= x < 50 and 0 <= y < 50 and t[x][y] not in seen:
#             seen.add(t[x][y])
#             search(starts, x,y,move+[dirs[i]],i)
#             seen.remove(t[x][y])
#
#     if len(redos):
#         raise BlockingIOError
#
# si,sj = SI,SJ
# move = []
# last = -1
# while time() - starttime < 1.95:
#     try:
#         search((SI,SJ), si, sj, move, last)
#     except BlockingIOError:
#         si,sj,move,last = redos.pop()
#     except ConnectionError:
#         pass
# print("".join(bmoves))

# while time() - starttime < 1.95:
#     # ランダム
#     shuffle(options)
#     for i in options:
#         x,y = si+dirmove[i][0], sj+dirmove[i][1]
#         if 0 <= x < 50 and 0 <= y < 50 and t[x][y] not in seen:
#             last = i
#             si,sj = x,y
#             moves.append(dirs[i])
#             seen.add(t[si][sj])
#             break
#     else:
#         break

# 最大の方に行く
# around = []
# if 0 < si:
#     around.append((t[si-1][sj], p[si-1][sj],1))
# if 0 < sj:
#     around.append((t[si][sj-1],p[si][sj-1],3))
# if si < 49:
#     around.append((t[si+1][sj],p[si+1][sj],0))
# if sj < 49:
#     around.append((t[si][sj+1],p[si][sj+1],2))
# around.sort(key=lambda T: T[1])
# for T,P,I in around:
#     x,y = si+dirmove[I][0], sj+dirmove[I][1]
#     if 0 <= x < 50 and 0 <= y < 50 and t[x][y] not in seen:
#         last = I
#         si,sj = x,y
#         moves.append(dirs[I])
#         seen.add(t[si][sj])
#         break

# 矢印と反対に行く
# if 0 < si and t[si][sj] == t[si-1][sj]:
#     x,y = si+dirmove[1][0], sj+dirmove[1][1]
#     if 0 <= x < 50 and 0 <= y < 50 and t[x][y] not in seen:
#         last = 1
#         si,sj = x,y
#         moves.append("D")
#         seen.add(t[si][sj])
#         continue
# if 0 < sj and t[si][sj] == t[si][sj-1]:
#     x,y = si+dirmove[3][0], sj+dirmove[3][1]
#     if 0 <= x < 50 and 0 <= y < 50 and t[x][y] not in seen:
#         last = 3
#         si,sj = x,y
#         moves.append("R")
#         seen.add(t[si][sj])
#         continue
# if si < 49 and t[si][sj] == t[si+1][sj]:
#     x,y = si+dirmove[0][0], sj+dirmove[0][1]
#     if 0 <= x < 50 and 0 <= y < 50 and t[x][y] not in seen:
#         last = 0
#         si,sj = x,y
#         moves.append("U")
#         seen.add(t[si][sj])
#         continue
# if sj < 49 and t[si][sj] == t[si][sj+1]:
#     x,y = si+dirmove[2][0], sj+dirmove[2][1]
#     if 0 <= x < 50 and 0 <= y < 50 and t[x][y] not in seen:
#         last = 2
#         si,sj = x,y
#         moves.append("L")
#         seen.add(t[si][sj])
#         continue