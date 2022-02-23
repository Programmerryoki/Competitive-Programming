from math import ceil

K = num = int(input())
pf = []
for n in range(1, ceil(K**0.5)):
    if num % n == 0:
        pf.append(n)
        if n != num // n:
            pf.append(num // n)
pf.sort()
# print(pf)

count = 0
for i in range(len(pf)):
    for j in range(i, len(pf)):
        a = pf[i]
        b = pf[j]
        if (K // a) < b:
            continue
        if K % (a * b) != 0:
            continue
        if b > K // (a * b):
            continue
        count += 1
print(count)