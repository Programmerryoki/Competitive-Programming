N = input()
i = len(N)-1
while i > 0 and N[i] == "0":
    i -= 1
N = N[i+1:] + N
print("Yes" if N == N[::-1] else "No")