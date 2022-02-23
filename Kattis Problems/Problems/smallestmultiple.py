from collections import defaultdict
from math import gcd

while True:
    try:
        nums = map(int, input().split())
    except:
        break

    # num = 1
    # for n in nums:
    #     num = (num * n) // gcd(num, n)
    # print(num)

    fact = defaultdict(int)
    for n in nums:
        temp = defaultdict(int)
        i = 2
        while n > 1:
            while n%i == 0:
                temp[i] += 1
                n //= i
            i += 1
        for key in temp:
            if fact[key] < temp[key]:
                fact[key] = temp[key]

    ans = 1
    for key in fact:
        bn = bin(fact[key])[2:]
        l = len(bn)
        mul = [key]*(l)
        for i in range(1,l):
            mul[i] = mul[i-1]**2
        for i in range(l):
            if bn[l-i-1] == "1":
                ans *= mul[i]
    print(ans)