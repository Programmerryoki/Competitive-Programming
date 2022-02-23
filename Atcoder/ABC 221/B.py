S = list(input())
T = list(input())
if S == T:
    print("Yes")
    exit()
for i in range(len(S)-1):
    if S[i] != T[i]:
        S[i],S[i+1]=S[i+1],S[i]
        if S != T:
            print("No")
            exit()
print("Yes")