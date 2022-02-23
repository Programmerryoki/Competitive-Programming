from sys import stdin

def main():
    input = stdin.readline
    N = int(input())
    tasks = [[int(i) for i in input().split()] for j in range(N)]
    tasks.sort()
    md = tasks[-1][0]
    dp = [-float("inf")]*(md+1)
    dp[0] = 0
    for i in range(N):
        dpn = [-float("inf")]*(md+1)
        D,C,S = tasks[i]
        for j in range(md):
            if dp[j] == -float("inf"):
                continue
            dpn[j] = max(dpn[j], dp[j])
            if j + C <= D:
                dpn[j+C] = max(dpn[j+C], dp[j] + S)
        dp = dpn
    print(max(dp))

if __name__ == '__main__':
    main()