S = input()
G = S.count("o")
B = len(S) - G
for s in S:
    print(100 * G / (G + B))
    if s == "o":
        G -= 1
    else:
        B -= 1