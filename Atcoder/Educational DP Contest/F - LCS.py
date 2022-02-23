def main():
    s = input()
    t = input()
    dp = [[0]*(len(s)+1) for i in range(len(t)+1)]
    for i in range(1,len(t)+1):
        for j in range(1,len(s)+1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    ans = ""
    i = len(t)
    j = len(s)
    while i != 0 and j != 0:
        if t[i-1] == s[j-1]:
            ans = t[i-1] + ans
            i -= 1
            j -= 1
        elif dp[i-1][j] < dp[i][j-1]:
            j -= 1
        else:
            i -= 1
    print(ans)

if __name__ == "__main__":
    main()