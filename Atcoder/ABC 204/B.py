N = int(input())
A = [int(i) for i in input().split()]
total = 0
for i in A:
    if i > 10:
        total += i - 10
print(total)