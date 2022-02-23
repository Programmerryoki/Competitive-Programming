def same(a,b):
    a,b = str(a), str(b)
    return a[0]==b[-1] and a[-1] == b[0]

N = int(input())
c = 0
for i in range(1,N+1):
    A = i
    valid = []
    for j in range(1,min(100, N+1)):
        if same(A, j):
            valid.append(j)

    for n in valid:
        if n <= N:
            # print(A, n)
            # print("\t",c)
            if n >= 100:
                if len(str(n)) < len(str(N)):
                    c += 10**(len(str(N)) - len(str(n))) - 1
                else:
                    c += 1
            else:
                c += 1
            # print("\t",c)
print(c)