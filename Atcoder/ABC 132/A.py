from collections import Counter
S = input()
cs = Counter(S)
if len(cs) == 2 and 2 in cs.values():
    print("Yes")
else:
    print("No")