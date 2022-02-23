S = list(input())
i,j = [int(i) for i in input().split()]
S[i], S[j] = S[j], S[i]
print("".join(S))