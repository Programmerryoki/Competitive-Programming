S = input()
link = [(0,0)]
t = []
for i,w in enumerate(S):
    if w == "(":
        t.append(i)
    elif w == ")":
        link.append((t.pop(), i))
print(link)

def dfs(ind):
    st = set()
    pst = set()
    s,e = link[ind]
    ps,pe = link[ind-1]
    while s < e:
        if ps <= s:
            s += pe - ps
            pst |= dfs(ind-1)
            st -= pst
        
        s += 1

try:
    dfs(0, [], set())
except:
    print("No")
else:
    print("Yes")