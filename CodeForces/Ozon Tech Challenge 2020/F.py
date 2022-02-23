from fractions import gcd

n = int(input())
a = [int(i) for i in input().split()]
g = a[0]
pos = [0, 0]
for i in a:
    g = gcd(g, i)
    pos[0] += i%2
    if i == 1:
        pos[1] += 2
    else:
        pos[1] += min(i%3, 1)
if g > 1:
    print(0)
else:
    print(min(pos))

# n = int(input())
# a = [int(i) for i in input().split()]
# g = a[0]
# pos = [0]*28
# for i in a:
#     g = gcd(g, i)
#     for a in range(2,30):
#         pos[a-2] += i%a
# if g > 1:
#     print(0)
# else:
#     print(min(pos))