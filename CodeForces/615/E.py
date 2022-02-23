import sys

def diff(a,b):
    d = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            d += 1
    return d

def main():
    input = sys.stdin.readline

    n, m = [int(i) for i in input().split()]
    grid = [[] for j in range(m)]
    for a in range(n):
        l = input().split()
        for b in range(m):
            grid[b].append(int(l[b]))

    count = 0
    for a in range(m):
        line = [i for i in grid[a]]
        optimal = [a+1+i*m for i in range(n)]
        d = diff(optimal, line)
        # print(line,optimal)
        c = 0
        temp = [0,0]
        while c <= d:
            line = line[1:] + line[:1]
            dn = diff(optimal, line)
            # print(d, dn, line, optimal)
            if dn < d:
                d = dn
                c += 1
            elif dn == d:
                d = dn
                if temp == 0:
                    temp = [c,d]
                c += 1
            else:
                break
        if temp[1] == d:
            c = temp[0]
        if c == d+1:
            count += d
        else:
            count += d + c
    print(count)

def maintest():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = [[] for i in range(m)]

    for _ in range(n):
        l = list(map(int, input().split()))
        for i in range(m):
            arr[i].append(l[i])

    out = 0
    for i in range(m):
        l = arr[i]

        best = list(range(0, -n, -1))
        for j in range(n):
            v = l[j] - i - 1

            if v % m == 0:
                correct = v // m
                if 0 <= correct < n:
                    best[j - correct] += 1
        out += (n - max(best))

    print(out)


if __name__ == "__main__":
    maintest()