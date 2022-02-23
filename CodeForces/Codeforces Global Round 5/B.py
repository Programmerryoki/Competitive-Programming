n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
dic = set()
fine = 0
for i in range(len(a)):
    dic.add(a[i])
    if a[i] == b[i]:
        if fine:
            fine += 1
        else:
            continue
    if not b[i] in dic:
        fine += 1
print(fine)