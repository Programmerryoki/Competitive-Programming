N = input()
mv = 0
for i in range(2**len(N)):
    num = bin(i)[2:][::-1]
    n1 = []
    n2 = []
    for i in range(len(N)):
        if i < len(num) and num[i] == "1":
            n1.append(N[i])
        else:
            n2.append(N[i])
    if n1 and n2:
        n1 = int("".join(sorted(n1,reverse=True)))
        n2 = int("".join(sorted(n2,reverse=True)))
        if n1 and n2:
            mv = max(mv, n1*n2)
print(mv)