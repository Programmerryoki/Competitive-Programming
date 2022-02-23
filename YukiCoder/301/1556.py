def pf(n, ori):
    num = {}
    for i in range(2, n+1):
        if n <= 1:
            break
        if n % i == 0:
            c = 0
            while n % i==0 and n > 1:
                n //= i
                c += 1
            # print(i, c, ori)
            num[i] = c * ori
    return num

A,B = [int(i) for i in input().split()]
dica = pf(A, B)
dicb = pf(B, A)
# print(dica, dicb)
print("Yes" if dica == dicb else "No")