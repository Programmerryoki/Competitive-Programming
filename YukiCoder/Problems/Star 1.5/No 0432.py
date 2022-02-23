T = int(input())
for _ in range(T):
    S = input()
    while len(S) != 1:
        t = ""
        for i in range(len(S)-1):
            n = int(S[i]) + int(S[i+1])
            t += str(n//10 + n%10)
        S = t
    print(S)