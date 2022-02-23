S = input()
print(sum([1 for i in range(len(S)) if S[i] != "CODEFESTIVAL2016"[i]]))