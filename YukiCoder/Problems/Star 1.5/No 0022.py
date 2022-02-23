N,K = [int(i) for i in input().split()]
S = input()
stack = []
for i in range(N):
    if S[i] == "(":
        stack.append(i)
    else:
        k = stack.pop()
        if i+1 == K or k+1 == K:
            print((i+1)^K^(k+1))