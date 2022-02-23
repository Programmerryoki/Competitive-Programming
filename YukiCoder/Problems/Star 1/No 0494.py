w = "yukicoder"
S = input()
for i in range(len(S)):
    if S[i] == "?":
        print(w[i])
        break