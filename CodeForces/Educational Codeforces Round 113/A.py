t = int(input())
for _ in range(t):
    n = int(input())
    S = input()
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            print(i+1, i+2)
            break
    else:
        print(-1, -1)