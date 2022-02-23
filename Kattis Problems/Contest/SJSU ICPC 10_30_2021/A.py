from sys import stdin

def main():
    input = stdin.readline
    N,P = map(float, input().split())
    N = int(N)
    boxes = [[float(i) for i in input().split()] for _ in range(N)]
    sb = int(sum([i[0] for i in boxes]))
    dp = [-float("inf")]*(sb+1)
    dp[0] = 0
    for i in range(N):
        new = [-float("inf")]*(sb+1)
        e,p = boxes[i]; e = int(e)
        for j in range(sb):
            if dp[j] == -float("inf"):
                continue
            if j + e <= sb:
                new[j+e] = max(new[j+e], dp[j] + p)
            new[j] = max(new[j], dp[j])
        dp = new
    for e in range(sb+1):
        if dp[e] >= P:
            print(e)
            exit()


if __name__ == '__main__':
    main()