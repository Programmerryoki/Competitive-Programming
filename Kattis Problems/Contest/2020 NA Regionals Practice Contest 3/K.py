n = int(input())
matrix = [input() for i in range(n)]

que = [0]
seen = [0]*n
seen[0] = 1
path = [-1]*n
while que:
    cur = que.pop()
    person = matrix[cur]
    for i in range(n):
        if not seen[i] and person[i] == "1":
            seen[i] = 1
            que.append(i)
            path[i] = cur


# n = int(input())
# matrix = [input() for i in range(n)]
#
# def bfs(cur, seen, order):
#     if len(seen) == n:
#         print(*order[::-1])
#         raise TypeError
#
#     person = matrix[cur]
#     for i in range(n):
#         if person[i] == "1" and i not in seen:
#             bfs(i, seen | {i}, order + [i])
#
# try:
#     bfs(0, {0}, [0])
#     print("impossible")
# except:
#     exit()