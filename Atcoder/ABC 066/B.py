S = input()
for i in range(len(S)//2-1, 0, -1):
    if S[:i] == S[i:i*2]:
        print(i*2)
        break