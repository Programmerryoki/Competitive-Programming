import re
S = input()
r = re.finditer("treeone",S)
for i in list(r)[::-1]:
    S = S[:i.start()] + "forest" + S[i.end():]
print(S)