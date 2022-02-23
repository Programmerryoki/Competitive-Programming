from collections import deque

N = int(input())
dis = [-1]*N
dis[0] = 1
que = deque([1])
seen = {1}
while que:
    node = que.popleft()
    move = bin(node).count("1")
    # print(node, move)
    if 0 < node - move and (node - move) not in seen:
        que.append(node - move)
        seen.add(node - move)
        dis[node - move - 1] = dis[node-1] + 1
    if node + move <= N and (node + move) not in seen:
        que.append(node + move)
        seen.add(node + move)
        dis[node + move - 1] = dis[node-1] + 1
# print(dis, seen)
print(dis[-1])