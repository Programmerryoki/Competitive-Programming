while True:
    p, c = [int(i) for i in input().split()]
    if p == c == 0:
        break

    graph = {i : set() for i in range(p)}
    for _ in range(c):
        a, b = [int(i) for i in input().split()]
        graph[a].add(b)
        graph[b].add(a)

    stack = [0]
    nodes = [i for i in range(p)]
    seen = set()
    path = {}
    while len(stack) != 0:
        # print(seen, stack, path)
        t = stack.pop()
        if t not in seen:
            seen.add(t)
            for n in graph[t]:
                if n not in seen:
                    path[n] = t
                    stack.append(n)
                # elif n != seen[-1]:
                elif path[t] != n:
                    # path[n] = t
                    # temp = path[t]
                    temp = t
                    # print(temp, n)
                    while temp != n:
                        # print(temp)
                        if temp in nodes:
                            nodes.remove(temp)
                        temp = path[temp]
                    if temp in nodes:
                        nodes.remove(temp)
    # print(nodes)
    if len(nodes) == 0:
        print("No")
    else:
        print("Yes")

# import sys
# sys.setrecursionlimit(5000)
#
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = []
#
# while True:
#     p, c = [int(i) for i in input().split()]
#     if p == c == 0:
#         break
#
#     graph = {i : set() for i in range(p)}
#     for _ in range(c):
#         a, b = [int(i) for i in input().split()]
#         graph[a].add(b)
#         graph[b].add(a)
#
#     tree = Node(0)
#     seen = set([0])
#     order = []
#
#     def dfs(root, t):
#         order.append(t)
#         for n in graph[t]:
#             if n not in seen:
#                 seen.add(n)
#                 node = Node(n)
#                 root.next.append(node)
#                 dfs(node, n)
#     dfs(tree,0)
#
#     if len(order) != p:
#         continue
#     graphb = graph
#
#     def const(root):
#         t = root.val
#         # print(t)
#         for n in root.next:
#             # graphb[n.val].add(t)
#             # graphb[t].add(n.val)
#             # graphb[n.val].remove(t)
#             graphb[t].remove(n.val)
#             const(n)
#     const(tree)
#
#     # stack = [order[-1]]
#     stack = [order[0]]
#     # seen = set([order[-1]])
#     seen = set([order[0]])
#     while len(stack) != 0:
#         t = stack.pop()
#         # print(t)
#         order.remove(t)
#         for n in graphb[t]:
#             if n not in seen:
#                 seen.add(n)
#                 stack.append(n)
#
#     if len(order) != 0:
#         print("Yes")
#     else:
#         print("No")