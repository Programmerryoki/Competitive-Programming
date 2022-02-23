from sys import stdin

def main():
    input = stdin.readline
    N = int(input())
    points = [[int(i) for i in input().split()] for j in range(N)]
    check = min(N, 3000)
    md = 0
    points.sort()
    for i in range(check):
        for j in range(check):
            if i == j:
                continue
            ix,iy = points[i]
            xi,yi = points[j]
            d = min(abs(ix-xi), abs(yi-iy))
            if d > md:
                md = d
    print(md)


if __name__ == '__main__':
    main()