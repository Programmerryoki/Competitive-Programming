from bisect import bisect_left, bisect_right

N,K,P = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
A.sort()
fhalf = A[:-(-N//2)]
resf = [[] for i in range(len(fhalf)+1)]
for n in range(2**len(fhalf)):
    num = bin(n)[2:][::-1]
    s = c = 0
    for i in range(len(num)):
        if num[i] == "1":
            s += fhalf[i]
            c += 1
    resf[c].append(s)

shalf = A[-(-N//2):]
ress = [[] for i in range(len(shalf)+1)]
for n in range(2**len(shalf)):
    num = bin(n)[2:][::-1]
    s = c = 0
    for i in range(len(num)):
        if num[i] == "1":
            s += shalf[i]
            c += 1
    ress[c].append(s)

for i in range(len(fhalf)+1):
    if i < len(ress):
        ress[i].sort()
    resf[i].sort()

# print(resf)
# print(ress)

count = 0
for i in range(min(K+1, len(resf))):
    other = K - i
    if other >= len(ress):
        continue
    for fs in resf[i]:
        ind = bisect_right(ress[other], P - fs)
        count += ind
print(count)