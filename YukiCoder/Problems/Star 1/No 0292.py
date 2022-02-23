S,t,u = input().split()
S = list(S)
S[int(t)] = ""
S[int(u)] = ""
print("".join(S))