def to9(N):
    N = str(N)
    num = 0
    for i in range(len(N)):
        num += int(N[i]) * 8**(len(N)-i-1)
    n = ""
    if num:
        while num > 0:
            n += str(num%9)
            num //= 9
    else:
        n = "0"
    return int("".join(i if i != "8" else "5" for i in n[::-1]))

N,K = [int(i) for i in input().split()]
for i in range(K):
    N = to9(N)
print(N)