from sys import stdin

def main():
    input = stdin.readline
    N = int(input())
    works = [tuple(int(i) for i in input().split()) for j in range(N)]
    works.sort()
    md = works[-1][0]
    dp = [-float("inf")]*(md+1)
    dp[0] = 0
    for i in range(N):
        new = [-float("inf")]*(md+1)
        for j in range(md):
            if dp[j] == -float("inf"):
                continue
            if dp[j] > new[j]:
                new[j] = dp[j]
            D,C,S = works[i]
            if j + C <= D:
                if dp[j] + S > new[j+C]:
                    new[j+C] = dp[j] + S
        dp = new
    print(max(dp))

if __name__ == '__main__':
    main()