S = input()
if S[3] != "-":
    print("No")
else:
    try:
        int(S[:3]+S[4:])
        print("Yes")
    except:
        print("No")