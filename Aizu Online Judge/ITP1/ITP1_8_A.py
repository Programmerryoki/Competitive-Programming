uw = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lw = "abcdefghijklmnopqrstuvwxyz"

S = list(input())
for i,a in enumerate(S):
    try:
        index = uw.index(a)
        S[i] = lw[index]
    except:
        try:
            index = lw.index(a)
            S[i] = uw[index]
        except:
            continue
print("".join(S))