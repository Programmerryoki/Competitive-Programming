n = int(input())
num = []
for a in range(n):
    num.append(int(input()))
mi = max(num) * 2
for a in range(n):
    if num[a] + num[(a + 2)%n] < mi:
        mi = num[a] + num[(a + 2)%n]
print(mi)