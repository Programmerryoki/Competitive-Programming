class AqaAsadiGroups:
    def minimumDifference(self, Skills, k):
        S = sum(Skills)
        dp = [[0]*(k+1) for i in range(len(Skills)+1)]
        for i in range(1, k+1):
            dp[0][i] = i * S**2
        for i in range(len(Skills)):
            for j in range(1,k+1):
                cur = 0
                dp[i+1][j] = float("inf")
                for l in range(i, -1, -1):
                    cur += Skills[l]
                    if j > 1 or l == 0:
                        dp[i+1][j] = min(dp[i+1][j], dp[l][j-1] + (cur*k - S)**2)
        # for i in dp:
        #     print(i)
        return dp[len(Skills)][k]

AAG = AqaAsadiGroups()
skills = (1,2,3,4)
print(AAG.minimumDifference(skills, 2))