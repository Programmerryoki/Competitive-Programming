S = input()
if S != S[::-1]:
    print("No")
elif S[:(len(S)-1)//2] != S[:(len(S)-1)//2][::-1]:
    print("No")
elif S[(len(S)+3)//2-1:] != S[(len(S)+3)//2-1:][::-1]:
    print("No")
else:
    print("Yes")