N = int(input())
S = input()
c = 0
for i in range(N):
    if S[i] == "U":
        for j in range(i+1,N):
            if S[j] == "M":
                k = 2*j - i
                if k < N:
                    if S[k] == "G":
                        c += 1
print(c)