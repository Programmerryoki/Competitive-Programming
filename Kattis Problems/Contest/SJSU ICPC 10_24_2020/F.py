from sys import stdin
from collections import defaultdict

def main():
    input = stdin.readline
    n,m = map(int, input().split())
    sticks = [set() for i in range(n)]
    have = [set() for i in range(n)]
    nn = defaultdict(set)
    nn[0] = set([i for i in range(n)])
    for _ in range(m):
        a,b = map(int, input().split())
        if a-1 not in sticks[b-1] and b-1 not in have[a-1]:
            sticks[b-1].add(a-1)
            have[a-1].add(b-1)
            nn[len(sticks[b-1])-1].remove(b-1)
            nn[len(sticks[b-1])].add(b-1)
        # print(nn)

    # print(sticks)
    # print(have)
    # print(nn)

    order = []
    total = set()
    while nn[0]:
        try:
            i = nn[0].pop()
            if i not in total:
                order.append(i+1)
                for N in have[i]:
                    sticks[N].discard(i)
                    nn[len(sticks[N])+1].remove(N)
                    nn[len(sticks[N])].add(N)
                total.add(i)
            if len(total) == n:
                break
        except:
            break
    if len(total) == n:
        print("\n".join(map(str, order)))
    else:
        print("IMPOSSIBLE")
if __name__ == "__main__":
    main()

# from collections import deque, defaultdict
#
# n,m = map(int, input().split())
# sticks = {i:set() for i in range(n)}
# have = [set() for i in range(n)]
# nn = defaultdict(set)
# nn[0] = set([i for i in range(n)])
# for _ in range(m):
#     a,b = map(int, input().split())
#     sticks[b-1].add(a-1)
#     have[a-1].add(b-1)
#     nn[len(sticks[b-1])-1].remove(b-1)
#     nn[len(sticks[b-1])].add(b-1)
#
# if len(nn[0]) != 0:
#     print("IMPOSSIBLE")
#     exit()
#
# print(sticks)
# print(have)
# print(nn)
#
# order = []
# total = set()
# while nn[0]:
#     i = nn[0].pop()
#     if i not in total and len(sticks[i]) == 0:
#         que = deque([i])
#         seen = set()
#         while que:
#             node = que.popleft()
#             order.append(node+1)
#             for N in have[node]:
#                 sticks[N].discard(node)
#                 if len(sticks[N]) == 0:
#                     que.append(N)
#             seen.add(node)
#         total.update(seen)
#     if len(total) == n:
#         break
# print("\n".join(map(str, order)))