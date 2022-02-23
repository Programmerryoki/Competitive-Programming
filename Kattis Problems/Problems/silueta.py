from bisect import bisect_left

N = int(input())
sss = [[int(i) for i in input().split()] for j in range(N)]
sss.sort()
start = [i[0] for i in sss]; end = [i[1] for i in sss]; height = [i[2] for i in sss]
mins = min(start); maxe = max(end); maxh = max(height)
grid = [["."]*(maxe) for i in range(maxh)]
mh = [[0]*2 for i in range(N)]
# construct picture
for L,R,H in sss:
    # The left most edge
    for i in range(H):
        grid[i][L] = "#"
    # the roof of ss
    for i in range(L,R):
        grid[H-1][i] = "#"
    # the right mose edge
    for i in range(H-1, -1, -1):
        grid[i][R-1] = "#"
grid = [i[mins:] for i in grid]
# for i in grid[::-1]:
#     print("".join(i))
# print("*"*(len(grid[-1])))

ans = [["."]*len(grid[0]) for i in range(len(grid))]
per = 0; pos = (0,-2)
while True:
    index = bisect_left(start, pos[1]+2)
    # print(index,start,pos)
    if index == N:
        break
    pos = tuple([-1,start[index]-mins]); fr = "T"
    prev = "";pp = (0,0); cc = 0; si = pos[1]
    # print("start:",pos, index, per)
    count = 0
    while not ((pos[0]==0 and prev == "B") or (pos[0] == 0 and not ((pos[1]+1 < len(grid[0]) and grid[pos[0]][pos[1]+1] == "#") or (pos[0]+1 < len(grid) and grid[pos[0]+1][pos[1]] == "#" and prev != "L")))):
        nx,ny = pos
        if fr == "T":
            if nx+1 < len(grid) and grid[nx+1][ny] == "#":
                fr, prev = "T", fr
                nx += 1
            elif ny+1 < len(grid[0]) and grid[nx][ny + 1] == "#":
                fr, prev = "L", fr
            elif nx+1 >= len(grid):
                fr, prev = "L", fr
        elif fr == "L":
            if nx + 1 < len(grid) and grid[nx+1][ny] == "#" and pp != pos: # and prev != "B":
                fr, prev = "T", fr
                nx += 1
            elif ny+1 < len(grid[0]) and grid[nx][ny+1] == "#":
                fr, prev = "L", fr
                ny += 1
            elif 0 <= nx - 1 and grid[nx-1][ny] == "#":
                fr, prev = "B", fr
        elif fr == "B":
            if ny+1 < len(grid[0]) and grid[nx][ny+1] == "#":
                fr, prev = "L", fr
                ny += 1
            elif 0 <= nx - 1 and grid[nx-1][ny] == "#":
                fr, prev = "B", fr
                nx -= 1
        pos,pp = (nx,ny),pos
        ans[nx][ny] = grid[nx][ny]
        count += 1
        if (fr == "T" and prev == "L") or (fr == "L" and prev == "B"):
            count -= 1
    #     print(pos, fr, count)
    #     for i in ans[::-1]:
    #         print("".join(i))
    #     print("*"*(len(ans[-1])))
    # print(pos, si)
    per += count
print(per)
for i in ans[::-1]:
    print("".join(i))
print("*"*(len(ans[-1])))

# from bisect import bisect_left
#
# N = int(input())
# sss = [[int(i) for i in input().split()] for j in range(N)]
# sss.sort()
# start = [i[0] for i in sss]; end = [i[1] for i in sss]; height = [i[2] for i in sss]
# mins = min(start); maxe = max(end); maxh = max(height)
# grid = [["."]*(maxe) for i in range(maxh)]
# mh = [[0]*2 for i in range(N)]
# # construct picture
# for L,R,H in sss:
#     # The left most edge
#     for i in range(H):
#         grid[i][L] = "#"
#     # the roof of ss
#     for i in range(L,R):
#         grid[H-1][i] = "#"
#     # the right mose edge
#     for i in range(H-1, -1, -1):
#         grid[i][R-1] = "#"
# grid = [i[mins:] for i in grid]
# for i in grid:
#     print("".join(i))
# print("*"*(len(grid[-1])))
#
# ans = [["."]*len(grid[0]) for i in range(len(grid))]
# per = 0; pos = (0,-2)
# while True:
#     index = bisect_left(start, pos[1]+2)
#     # print(index,start,pos)
#     if index == N:
#         break
#     pos = tuple([-1,start[index]-mins]); fr = "T"
#     prev = "";pp = (0,0); cc = 0; si = pos[1]
#     print("start:",pos, index, per)
#     h = 0
#     while not (pos[0] == 0 and not ((pos[1]+1 < len(grid[0]) and grid[pos[0]][pos[1]+1] == "#") or (pos[0]+1 < len(grid) and grid[pos[0]+1][pos[1]] == "#" and prev != "L"))):
#         nx,ny = pos
#         if fr == "T":
#             if nx+1 < len(grid) and grid[nx+1][ny] == "#":
#                 nx += 1
#             elif ny+1 < len(grid[0]) and grid[nx][ny + 1] == "#":
#                 fr, prev = "L", fr
#             elif nx+1 >= len(grid):
#                 fr, prev = "L", fr
#         elif fr == "L":
#             if nx + 1 < len(grid) and grid[nx+1][ny] == "#" and pp != pos: # and prev != "B":
#                 fr, prev = "T", fr
#                 nx += 1
#             elif ny+1 < len(grid[0]) and grid[nx][ny+1] == "#":
#                 ny += 1
#             elif 0 <= nx - 1 and grid[nx-1][ny] == "#":
#                 fr, prev = "B", fr
#         elif fr == "B":
#             if ny+1 < len(grid[0]) and grid[nx][ny+1] == "#":
#                 fr, prev = "L", fr
#             elif 0 <= nx - 1 and grid[nx-1][ny] == "#":
#                 nx -= 1
#         pos,pp = (nx,ny),pos
#         h = max(h,nx)
#         ans[nx][ny] = grid[nx][ny]
#         print(pos, fr)
#         for i in ans[::-1]:
#             print("".join(i))
#         print("*"*(len(ans[-1])))
#     print(pos, si, h)
#     h += 1
#     # print(2*h + (pos[1] + 1 - si))
#     per += 2*h + (pos[1] + 1 - si)
# print(per)
# for i in ans[::-1]:
#     print("".join(i))
# print("*"*(len(ans[-1])))

# from bisect import bisect_left
#
# N = int(input())
# sss = [[int(i) for i in input().split()] for j in range(N)]
# sss.sort()
# start = [i[0] for i in sss]; end = [i[1] for i in sss]; height = [i[2] for i in sss]
# mins = min(start); maxe = max(end); maxh = max(height)
# grid = [["."]*(maxe) for i in range(maxh)]
# mh = [[0]*2 for i in range(N)]
# # construct picture
# for L,R,H in sss:
#     # The left most edge
#     for i in range(H):
#         grid[i][L] = "#"
#     # the roof of ss
#     for i in range(L,R):
#         grid[H-1][i] = "#"
#     # the right mose edge
#     for i in range(H-1, -1, -1):
#         grid[i][R-1] = "#"
# grid = [i[mins:] for i in grid]
# for i in grid:
#     print("".join(i))
# print("*"*(len(grid[-1])))
#
# ans = [["."]*len(grid[0]) for i in range(len(grid))]
# per = 0; pos = (0,0)
# while True:
#     index = bisect_left(start, pos[1])
#     if index == N:
#         break
#     pos = tuple([-1,start[index]-mins]); fr = "T"
#     count = 0; prev = ""; cc = 0
#     print("start:",pos, index, per)
#     while not (pos[0] == 0 and not ((pos[1]+1 < len(grid[0]) and grid[pos[0]][pos[1]+1] == "#") or (pos[0]+1 < len(grid) and grid[pos[0]+1][pos[1]] == "#" and prev != "L"))):
#         nx,ny = pos
#         if fr == "T":
#             if nx+1 < len(grid) and grid[nx+1][ny] == "#":
#                 nx += 1
#             elif ny+1 < len(grid[0]) and grid[nx][ny + 1] == "#":
#                 fr, prev = "L", fr
#             elif nx+1 >= len(grid):
#                 fr, prev = "L", fr
#         elif fr == "L":
#             if nx + 1 < len(grid) and grid[nx+1][ny] == "#" and prev != "B":
#                 fr, prev = "T", fr
#                 count -= 2
#             elif ny+1 < len(grid[0]) and grid[nx][ny+1] == "#":
#                 ny += 1
#             elif 0 <= nx - 1 and grid[nx-1][ny] == "#":
#                 fr, prev = "B", fr
#         elif fr == "B":
#             if ny+1 < len(grid[0]) and grid[nx][ny+1] == "#":
#                 fr, prev = "L", fr
#                 count -= 2
#             elif 0 <= nx - 1 and grid[nx-1][ny] == "#":
#                 nx -= 1
#         count += 1
#         pos = (nx,ny)
#         ans[nx][ny] = grid[nx][ny]
#         print(pos,count)
#         for i in ans[::-1]:
#             print("".join(i))
#         print("*"*(len(ans[-1])))
#     per += count
#     # print(per)
#     # if fr == "B" and pos == (0,len(grid[0])):
#     #     break
# print(per)
# for i in ans[::-1]:
#     print("".join(i))
# print("*"*(len(ans[-1])))

# from bisect import bisect_left
#
# N = int(input())
# sss = [[int(i) for i in input().split()] for j in range(N)]
# sss.sort()
# # print(sss)
# start = [i[0] for i in sss]; end = [i[1] for i in sss]; height = [i[2] for i in sss]
# mins = min(start)
# maxe = max(end)
# maxh = max(height)
# grid = [["."]*(maxe+1) for i in range(maxh)]
# mh = [[0]*2 for i in range(N)]
# # for i in grid:
# #     print(i)
# for I,[L,R,H] in enumerate(sss):
#     mhs, mhe = mh[I]
#     # The left most edge
#     for i in range(H):
#         if i < mhs:
#             continue
#         grid[i][L] = "#"
#
#     index = bisect_left(start,L)
#     # the roof of ss
#     s = start[index]; e = 0; h = 0
#     for i in range(L,R):
#         print(i,e,H,h)
#         if index < N and i == start[index]:
#             e = end[index]
#             h = height[index]
#             # grid[H-1][i] = "#"
#             if H < h:
#                 mh[index][0] = H-1
#             index += 1
#             continue
#         if i < e and H < h:
#             continue
#         grid[H-1][i] = "#"
#
#     index = bisect_left(end, R)
#     # the right mose edge
#     for i in range(H-1, -1, -1):
#         if i < mhe:
#             break
#         grid[i][R] = "#"
#
#     print(mhs, mhe)
#     for i in grid[::-1]:
#         print("".join(i))
#     print()
# for i in grid[::-1]:
#     print("".join(i[mins:]))
# print("*"*(len(grid[-1]) - mins))