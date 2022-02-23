# from fractions import gcd
#
# a,b,c = [int(i) for i in input().split()]
# a = float.as_integer_ratio(a**0.5)
# b = float.as_integer_ratio(b**0.5)
# c = float.as_integer_ratio(c**0.5)
# lcm = a[1]*b[1]//gcd(a[1], b[1])
# ab = [a[0]*lcm//a[1] + b[0]*lcm//b[1], lcm]
# ans = ab[1]*c[1]//gcd(ab[1], c[1])
# if ab[0]*ans//ab[1] < c[0]*ans//c[1]:
#     print("Yes")
# else:
#     print("No")

# a,b,c = [int(i) for i in input().split()]
# if round(a**0.5 + b**0.5, 10) < round(c**0.5, 10):
#     print("Yes")
# else:
#     print("No")

# a,b,c = [int(i) for i in input().split()]
# if a**0.5 + b**0.5 < c**0.5:
#     print("Yes")
# else:
#     print("No")


a,b,c = [int(i) for i in input().split()]
if (a * b)**0.5//1 < c - (a + b):
    print("Yes")
else:
    print("No")