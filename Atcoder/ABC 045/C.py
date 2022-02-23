S = list(input())
if len(S) != 1:
    t = 0
    for n in range(2**(len(S) - 1)):
        f = S[0]
        b = bin(n)[2:]
        b = "0"*(len(S) - len(b) - 1) + b
        for a in range(len(b)):
            if b[a] == "1":
                f += "+"
            f += S[a+1]
        t += eval(f)
    print(t)
else:
    print(S[0])