S = input()
if len(S)&1:
    print("NO")
else:
    for i in range(len(S)//2):
        if S[i] != S[i+len(S)//2]:
            print("NO")
            break
    else:
        print("YES")