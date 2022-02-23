S = input()
i = -1
c = 0
while i < len(S):
    try:
        i = S.index("mi", i+1)
        i = S.index("n", i+1)
        c += 1
    except:
        break
print(c)