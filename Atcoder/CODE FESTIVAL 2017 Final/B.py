from collections import Counter

S = input()
CS = Counter(S)
if max(abs(CS["a"]-CS["b"]), abs(CS["a"]-CS["c"]), abs(CS["b"]-CS["c"])) <= 1:
    print("YES")
else:
    print("NO")