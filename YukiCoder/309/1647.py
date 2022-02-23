from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

def main():
    input = stdin.readline
    H,W,N = [int(i) for i in input().split()]
    odd = {}
    even = {}
    points = []
    for ind in range(N):
        x,y = [int(i) for i in input().split()]
        points.append((x,y))
        if x not in even:
            even[x] = set()
        if y not in odd:
            odd[y] = set()
        for i,j in points:
            if i == x:
                even[i].add(ind+1)
                even[x].add(ind+1)
            if j == y:
                odd[j].add(ind+1)
                odd[y].add(ind+1)

    # print(odd)
    # print(even)

    start = 0
    seen = set()
    def dfs(x,y):
        nonlocal seen
        rodd = len(seen)&1
        graph = odd if rodd else even
        nxt = y if rodd else x
        for n in graph[nxt]:
            if n not in seen:
                seen.add(n)
                i,j = points[n-1]
                lst = dfs(i,j)
                if lst is not None:
                    print(lst)
                    lst.append(n)
                    return lst
                seen.remove(n)
            else:
                if n == start:
                    return []
        return None

    start = 1
    seen.add(1)
    lst = dfs(points[0][0], points[0][1])
    if lst:
        print(len(lst))
        print(" ".join(str(i) for i in lst))
    else:
        print(-1)

import cProfile
cProfile.run('main()')
# if __name__ == '__main__':
#     main()