N, K = [int(i) for i in input().split()]
n = N//K
num = N%K
if num > K - num:
    num = K - num
    n += 1

print(num)