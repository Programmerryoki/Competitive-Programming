from collections import deque

N = int(input())
graph = {}
for _ in range(N):
    st = input().split()
    try:
        graph[st[0]].update(set(st[1:]))
    except:
        graph[st[0]] = set(st[1:])
    for n in st[1:]:
        try:
            graph[n].add(st[0])
        except:
            graph[n] = set(st[:1])
# print(graph)
try:
    s,e = input().split()
    que = deque([s])
    path = {s:""}
    seen = set()
    t = ""
    while len(que) != 0:
        t = que.popleft()
        if t == e:
            break
        seen.add(t)
        for n in graph[t]:
            if n not in seen:
                path[n] = t
                que.append(n)
    if t == e:
        ans = deque()
        prev = e
        while prev != "":
            ans.appendleft(prev)
            prev = path[prev]
        print(" ".join(ans))
    else:
        print("no route found")
except:
    print("no route found")

# N = int(input())
# station = []
# for _ in range(N):
#     st = input().split()
#     if len(st) != 2:
#         connect = [[],[]]
#         m, a, *rest = st
#         b = rest[-1]
#         for i,r in enumerate(station):
#             if m == r[0]:
#                 if a == r[1]:
#                     station[i] = [b] + rest[::-1] + station[i]
#                     connect[1] = [i, 1]
#                 elif b == r[1]:
#                     station[i] = [a] + rest + station[i]
#                     connect[0] = [i, 1]
#             elif m == r[-1]:
#                 if a == r[-2]:
#                     station[i] += rest + [b]
#                     connect[1] = [i, -1]
#                 elif b == r[-2]:
#                     station[i] += rest[::-1] + [a]
#                     connect[0] = [i, -1]
#             else:
#                 if r[0] == a:
#                     connect[0] = [i, 1]
#                 elif r[-1] == a:
#                     connect[0] = [i, -1]
#                 elif r[0] == b:
#                     connect[1] = [i, 1]
#                 elif r[-1] == b:
#                     connect[1] = [i, -1]
#         if connect == [[],[]]:
#             station.append([a,m,b])
#         elif len(connect[0]) != 0 and len(connect[1]) != 0:
#             i,p1 = connect[0]
#             j,p2 = connect[1]
#             station[i] = station[i][::-p1] + station[j][::p2]
#             del station[j]
#     else:
#         m, a = st
#         for i,r in enumerate(station):
#             if r[0] == a:
#                 station[i] = [m] + station[i]
#             elif r[-1] == a:
#                 station[i] += [m]
#
# print(station)
# s,d = input().split()
# for r in station:
#     if r[0] == s and r[-1] == d:
#         print(" ".join(r))
#         break
#     elif r[-1] == s and r[0] == d:
#         print(" ".join(r[::-1]))
#         break
# else:
#     print("no route found")