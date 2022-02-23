from sys import stdin

def main():
    N, M, Q = map(int, input().split())
    inp = stdin.readlines()
    X = [int(i) for i in inp[-1].split()]
    mx = max(X)
    graph = {i: {} for i in range(N)}
    for line in inp[:-1]:
        A, B, C = map(int, line.split())
        if C > mx:
            continue
        graph[A-1][B-1] = C
        graph[B-1][A-1] = C

    base = 0
    ans = [""] * Q
    que = {0}
    for day, xt in enumerate(X):
        new = set()
        qr = set()
        for index in que:
            gindex = graph[index]
            if not gindex:
                qr.add(index)
                base += 1
                continue
            remove = set()
            for node in gindex:
                if node in que:
                    continue
                elif gindex[node] <= xt:
                    new.add(node)
                    remove.add(node)
            for r in remove:
                del gindex[r]
        que -= qr
        que |= new
        if len(que) + base == N:
            ans[day:] = [str(N)]*(Q - day)
            break
        ans[day] += str(len(que) + base)
    print("\n".join(ans))

if __name__ == "__main__":
    main()