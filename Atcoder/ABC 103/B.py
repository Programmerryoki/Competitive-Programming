S = input()
T = input()
pos = False
i = -1
while True:
    try:
        i = T.index(S[0], i+1)
        if T[i:] + T[:i] == S:
            print("Yes")
            break
    except:
        print("No")
        break