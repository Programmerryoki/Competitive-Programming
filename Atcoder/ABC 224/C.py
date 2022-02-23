from sys import stdin

def main():
    input = stdin.readline
    N = int(input())
    points = [[int(i) for i in input().split()] for _ in range(N)]
    count = 0
    for i in range(N):
        x1,y1 = points[i]
        for j in range(i+1,N):
            x2,y2 = points[j]
            d1 = [x2 - x1, y2 - y1]
            for k in range(j+1, N):
                x3,y3 = points[k]
                d2 = [x3 - x1, y3 - y1]
                if d1[0] * d2[1] - d1[1] * d2[0] != 0:
                    count += 1
    print(count)


if __name__ == '__main__':
    main()