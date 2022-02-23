from sys import stdin

def main():
    input = stdin.readline
    H,W,C = [int(i) for i in input().split()]
    # A = [[int(i) for i in input().split()] for j in range(H)]
    A = []
    m = float("inf")
    mins = []
    for i in range(H):
        isp = input().split()
        tp = []
        for j in range(W):
            iis = int(isp[j])
            if iis < m:
                m = iis
                mins = [(i,j)]
            elif iis == m:
                mins.append((i,j))
            tp.append(iis)
        A.append(tp)

    def mingrid(oi,oj):
        mins = []
        mi = float("inf")
        for i in range(H):
            for j in range(W):
                calc = C * (abs(i-oi) + abs(oj-j)) + A[i][j] + A[oi][oj]
                if i != oi or j != oj:
                    if calc < mi:
                        mi = calc
                        mins = [(i,j)]
                    elif calc == mi:
                        mins.append((i,j))
        return mi, mins

    # m,min = mingrid((0,0))
    # am = m
    # seen = {(0,0)}
    am = float("inf")
    seen = set()
    while mins:
        i,j = mins.pop()
        if (i,j) in seen:
            continue
        seen.add((i,j))
        m,mi = mingrid(i,j)
        if am > m:
            am = m
            mins = mi + mins
    print(am)


if __name__ == '__main__':
    main()