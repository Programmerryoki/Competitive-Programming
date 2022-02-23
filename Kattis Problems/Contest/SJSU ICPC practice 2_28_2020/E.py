from math import ceil

n,q = [int(i) for i in input().split()]
primes = [2]
for a in range(3,n+2,2):
    m = int(a**0.5)+1
    for b in primes:
        if a%b==0:
            break
        elif b >= m:
            primes.append(a)
            break
    else:
        primes.append(a)

def index(n):
    i = ceil(len(primes)/2)
    s = ceil(len(primes)/4)
    on = True
    while s != 0:
        # print(i, primes[i])
        if primes[i] == n:
            return 1
        elif primes[i] > n:
            i -= s
        else:
            i += s
        if i < 0:
            i = 0
        elif i >= len(primes):
            i = len(primes)
        if s != 1:
            s = ceil(s/2)
        else:
            if not on:
                break
            else:
                on = False
    return 0

print(len(primes))
for _ in range(q):
    x = int(input())
    print(index(x))

# primes = bytearray([1]*(n+1))
# count = 0
#
# primes[0] = 0
# primes[1] = 0
#
# i = 0
# while True:
#     try:
#         i = primes.index(1,i+1)
#     except:
#         break
#     count += 1
#     for a in range(2*i,n+1,i):
#         primes[a] = 0
# print(count)
# print(len(primes))
# for _ in range(q):
#     x = int(input())
#     print(primes[x])