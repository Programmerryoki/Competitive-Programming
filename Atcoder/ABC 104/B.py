S = input()
if S[0] != "A":
    print("WA")
    exit()
if S[2:-1].count("C") != 1:
    print("WA")
    exit()
if (S[1:S.index("C",2)] + S[S.index("C",2)+1:]).islower():
    print("AC")
else:
    print("WA")