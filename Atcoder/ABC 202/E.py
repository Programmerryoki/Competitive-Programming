from sys import stdin

def main():
    input = stdin.readline
    N = int(input())
    parents = [-1]+[int(i)-1 for i in input().split()]
    child = {i:set() for i in range(N)}
    for i in range(1,N):
        child[parents[i]].add(i)

    dist = [float("inf")]*N
    dist[0] = 0
    que = [0]
    while que:
        node = que.pop()
        for n in child[node]:
            dist[n] = dist[node] + 1
            que.append(n)
    maxd = max(dist)
    # print(child)
    # print(dist)
    Q = int(input())
    ans = [0]*Q
    for case,line in enumerate(stdin.readlines()):
        line = line.strip()
        U,D = [int(i)-1 for i in line.split()]
        D += 1
        if dist[U] == D:
            ans[case] = 1
            continue
        if dist[U] > D:
            continue
        if D > maxd:
            continue
        que = [U]
        count = 0
        while que:
            # print(que)
            node = que.pop()
            # print(node,child[node])
            for n in child[node]:
                # print(n)
                if dist[n] < D:
                    que.append(n)
                    # print("added")
                elif dist[n] == D:
                    count += 1
        ans[case] = count
    print("\n".join(map(str, ans)))

if __name__ == '__main__':
    main()