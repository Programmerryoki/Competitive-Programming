S = input()
ml = float("INF")
for i in range(0,len(S)):
    for j in range(1,len(S)+1):
        try:
            k = S[i:j].index("c")
            k = S[i:j].index("w", k)
            k = S[i:j].index("w",k+1)
            ml = min(ml, j - i)
        except:
            continue
print(ml if ml != float("INF") else -1)