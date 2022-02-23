MOD = 10**9 + 7

T = int(input())
for case in range(T):
    N,K = map(int, input().split())
    S = input()
    pos = {""}
    for i in range(N//2 + (N&1)):
        npos = set()
        for s in pos:
            for j in range(K):
                w = chr(ord("a")+j)
                npos.add(s+w)
        pos = npos
    tmp = set()
    for s in pos:
        tmp.add(s + (s[:-1][::-1] if N&1 else s[::-1]))
    print(f"Case #{case+1}: {sum([1 for i in tmp if i < S]) % MOD}")

# MOD = 10**9 + 7
#
# T = int(input())
# for case in range(T):
#     N,K = map(int, input().split())
#     S = input()
#     #=====================================================
#     pos = {""}
#     for i in range(N//2 + (N&1)):
#         npos = set()
#         for s in pos:
#             for j in range(K):
#                 w = chr(ord("a")+j)
#                 npos.add(s+w)
#         pos = npos
#     tmp = set()
#     for s in pos:
#         tmp.add(s + (s[:-1][::-1] if N&1 else s[::-1]))
#     # print(tmp)
#     print("ANS:", sum([1 for i in tmp if i < S]))
#     #=====================================================
#
#     dp = [[0,0] for i in range(N//2 + (N&1) + 1)]
#     # print(dp)
#     # dp[0] = [1, min(ord(S[0]), ord(S[-1])) - ord("a")]
#     dp[0] = [1,0]
#     issame = True
#     for i in range(1, N//2 + (N&1) + 1):
#         if S[i-1] != S[len(S)-i]:
#             issame = False
#         dp[i][1] = dp[i-1][1] * K
#         dp[i][1] += dp[i-1][0] * ( - ord("a")) #+ (S[i-1] != S[len(S)-i]))
#         print(i-1,S[i-1],len(S)-i, S[len(S)-i], min(ord(S[i-1]), ord(S[len(S)-i])) - ord("a"))
#         dp[i][0] += 1
#
#         dp[i][1] %= MOD
#         dp[i][0] %= MOD
#         print(dp[i])
#     print(dp)
#     print(f"Case #{case+1}: {dp[-1][1] % MOD + int(not issame)}")
#
# """
# 10
# 8 5
# eebbdeca
# """