S = input()
m = 0
p = ""
con = 0
for i in range(len(S)):
    if S[i] == p:
        con += 1
    else:
        m = max(con, m)
        con = 0
