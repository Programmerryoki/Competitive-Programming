# from sys import getsizeof as gso
# size = 1000
# pos = [[1]*5 for i in range(5)]
# pos[1][1] = 0; pos[2][3] = 0
# print(gso(pos)*(25**5))
# tuples = tuple([tuple([i,j]) for i in range(5) for j in range(5) if pos[i][j] == 1])
# print(gso(tuples))
#
# print(gso([i for i in range(size)]))
# print(gso(" ".join(map(str, [i for i in range(size)]))))
# print(gso(set([i for i in range(size)])))

from sys import stdin

def main():
    input = stdin.readline
    N,K = map(int, input().split())
    grid = [input() for i in range(N)]
    ships = [int(input()) for i in range(K)]
    used = []
    reu = set()
    for i in range(N):
        for j in range(N):
            if grid[i][j] == "X":
                used.append(tuple([i,j]))
            elif grid[i][j] == "O":
                reu.add(tuple([i,j]))
    used.sort()
    used = tuple(used)
    pos = {used : 1}
    for sp in ships:
        new = {}
        for p in pos:
            for i in range(N):
                for j in range(N):
                    if i + sp <= N:
                        vl = sum([tuple([i+k,j]) in p for k in range(sp)])
                        if vl == 0:
                            temp = [i for i in p]
                            for k in range(sp):
                                temp.append(tuple([i+k,j]))
                            temp.sort()
                            temp = tuple(temp)
                            new.setdefault(temp, 0)
                            new[temp] += pos[p]
                    if sp != 1 and j + sp <= N:
                        hl = sum([tuple([i,j+k]) in p for k in range(sp)])
                        if hl == 0:
                            temp = [i for i in p]
                            for k in range(sp):
                                temp.append(tuple([i,j+k]))
                            temp.sort()
                            temp = tuple(temp)
                            new.setdefault(temp, 0)
                            new[temp] += pos[p]
        pos = new
    c = 0
    for p in pos:
        if len(reu - set(p)) == 0:
            c += pos[p]
    print(c)

if __name__ == "__main__":
    main()


# N,K = map(int, input().split())
# grid = [input() for i in range(N)]
# ships = [int(input()) for i in range(K)]
# used = []
# reu = set()
# for i in range(N):
#     for j in range(N):
#         if grid[i][j] == "X":
#             used.append(tuple([i,j]))
#         elif grid[i][j] == "O":
#             reu.add(tuple([i,j]))
# pos = [used]
# for sp in ships:
#     new = []
#     for p in pos:
#         for i in range(N):
#             for j in range(N):
#                 if i + sp <= N:
#                     vl = sum([tuple([i+k,j]) in p for k in range(sp)])
#                     if vl == 0:
#                         temp = [i for i in p]
#                         for k in range(sp):
#                             temp.append(tuple([i+k,j]))
#                         new.append(temp)
#                 if sp != 1 and j + sp <= N:
#                     hl = sum([tuple([i,j+k]) in p for k in range(sp)])
#                     if hl == 0:
#                         temp = [i for i in p]
#                         for k in range(sp):
#                             temp.append(tuple([i,j+k]))
#                         new.append(temp)
#     pos = new
# c = 0
# for p in pos:
#     if len(reu - set(p)) == 0:
#         c += 1
# print(c)


# from copy import deepcopy
# import sys
# sys.setrecursionlimit(10**8)
#
# N,K = map(int, input().split())
# grid = [input() for i in range(N)]
# used = {}
# reu = set()
# for i in range(N):
#     for j in range(N):
#         if grid[i][j] == "X":
#             used[tuple([i,j])] = "X"
#         elif grid[i][j] == "O":
#             reu.add(tuple([i,j]))
#
# ships = [int(input()) for i in range(K)]
# ans = []
#
# def recur(ug, rug, sp):
#     # for i in ug:
#     #     print(i)
#
#     global ans
#     if sp == len(ships):
#         if len(rug) == 0 and ug not in ans:
#             # print(ug.keys())
#             ans.append(ug)
#         return
#
#     for i in range(N):
#         for j in range(N):
#             if not tuple([i,j]) in ug:
#                 if i + ships[sp] <= N:
#                     # print([tuple([i+k,j]) for k in range(ships[sp])])
#                     # print([tuple([i+k,j]) in ug for k in range(ships[sp])])
#                     vl = sum([tuple([i+k,j]) in ug for k in range(ships[sp])])
#                     if vl == 0:
#                         tug = deepcopy(ug)
#                         for k in range(ships[sp]):
#                             tug[tuple([i+k,j])] = str(sp)
#                         trug = deepcopy(rug)
#                         trug -= set(tug.keys())
#                         recur(tug, trug, sp+1)
#
#                 if j + ships[sp] <= N:
#                     # print([tuple([i,j+k]) for k in range(ships[sp])])
#                     # print([tuple([i,j+k]) in ug for k in range(ships[sp])])
#                     hl = sum([tuple([i,j+k]) in ug for k in range(ships[sp])])
#                     if hl == 0:
#                         tug = deepcopy(ug)
#                         for k in range(ships[sp]):
#                             tug[tuple([i,j+k])] = str(sp)
#                         trug = deepcopy(rug)
#                         trug -= set(tug.keys())
#                         recur(tug, trug, sp+1)
#
# recur(used, reu, 0)
# print(len(ans))
# # print(ans)


# from copy import deepcopy
# import sys
# sys.setrecursionlimit(10**9)
#
# N,K = map(int, input().split())
# grid = [list(input()) for i in range(N)]
# ships = [int(input()) for i in range(K)]
# all = set()
# total = set()
# smaker = lambda x: "\n".join("".join(i) for i in x)
#
# def recur(gd, sp):
#     global total
#     if sp == len(ships):
#         return
#
#     for i in range(N):
#         for j in range(N):
#             if gd[i][j] in ["O","."]:
#                 if i + ships[sp] <= N:
#                     vl = [gd[i+k][j] for k in range(ships[sp])]
#                     if len(set(vl) - {"O", "."}) == 0:
#                         temp = deepcopy(gd)
#                         for k in range(ships[sp]):
#                             temp[i+k][j] = str(sp)
#                         string = smaker(temp)
#                         if sp == len(ships)-1 and "O" not in string:
#                             total.add(string)
#                         recur(temp, sp + 1)
#                 if j + ships[sp] <= N:
#                     hl = deepcopy(gd[i][j:j+ships[sp]])
#                     if len(set(hl) - {"O", "."}) == 0:
#                         temp = deepcopy(gd)
#                         for k in range(ships[sp]):
#                             temp[i][j+k] = str(sp)
#                         string = smaker(temp)
#                         if sp == len(ships)-1 and "O" not in string:
#                             total.add(string)
#                         recur(temp, sp + 1)
#
#
# recur(grid, 0)
# print(len(total))
# # for i in total:
# #     print(i)
# #     print()


# from copy import deepcopy
# import sys
# sys.setrecursionlimit(10**8)
#
# N,K = map(int, input().split())
# grid = [list(input()) for i in range(N)]
# ships = [int(input()) for i in range(K)]
# tn = {}
# total = 0
# smaker = lambda x: "\n".join("".join(i) for i in x)
#
# def recur(gd, sp, tn):
#     global total
#     if sp == len(ships):
#         # if sp-1 >= 0:
#         #     print(ships[sp-1])
#         # print(smaker(gd))
#         # print()
#         return
#
#     for i in range(N):
#         for j in range(N):
#             if gd[i][j] in ["O","."]:
#                 if i + ships[sp] <= N:
#                     vl = [gd[i+k][j] for k in range(ships[sp])]
#                     if len(set(vl) - {"O", "."}) == 0:
#                         temp = deepcopy(gd)
#                         for k in range(ships[sp]):
#                             temp[i+k][j] = str(sp)
#                         string = smaker(temp)
#                         if not string in tn:
#                             tn.setdefault(string, {})
#                             if sp == len(ships)-1 and "O" not in string:
#                                 total += 1
#                         recur(temp, sp+1, tn[string])
#                 if j + ships[sp] <= N:
#                     hl = deepcopy(gd[i][j:j+ships[sp]])
#                     if len(set(hl) - {"O", "."}) == 0:
#                         temp = deepcopy(gd)
#                         for k in range(ships[sp]):
#                             temp[i][j+k] = str(sp)
#                         string = smaker(temp)
#                         if not string in tn:
#                             tn.setdefault(string, {})
#                             if sp == len(ships)-1 and "O" not in string:
#                                 total += 1
#                         recur(temp, sp+1, tn[string])
#
# recur(grid, 0, tn)
# print(total)