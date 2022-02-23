x = int(input())

n = int(input())
left = x
for a in range(n):
    left += x - int(input())
print(left)