from bisect import bisect_right

num = int(input())
fac = []
fab = []
for i in range(1,int(num**0.5)+1):
    if num%i==0:
        fac.append(i)
        if num//i != i:
            fab.append(num//i)
fac.extend(fab[::-1])
print(fac)
fs = set(fac)
ans = set()
for i in fs:
    for j in fs:
        ans.add(i*j)
        ans.add(2*i)
        ans.add(2*j)
f = list(ans | fs)
f.sort()
print(f)
print(bisect_right(f, num))