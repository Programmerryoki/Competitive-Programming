from math import gcd
N,X = [int(i) for i in input().split()]
x = [abs(int(i)-X) for i in input().split()]
n = x[0]
for p in x:
    n = gcd(p, n)
print(n)

# N,X = [int(i) for i in input().split()]
# x = [int(i) for i in input().split()]
#
# def possible(D):
#     for p in x:
#         if abs(X - p) % D != 0:
#             return False
#     return True
#
# left = 1
# right = 10**9
# while left < right:
#     mid = (left + right) // 2
#     print(left, right, mid)
#     if possible(mid):
#         left = mid + 1
#     else:
#         right = mid - 1
# print(left)