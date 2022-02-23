# N, M = [int(i) for i in input().split()]
# a = set(input().split())
# a = list(map(lambda x: int(x)//2, a))
# c = 1
# for n in a:
#     c *= n
# print(c)
# print(M//c - M//(c*2))

from fractions import gcd
from functools import reduce
import sys
def main():
    input = sys.stdin.readline
    N, M = [int(i) for i in input().split()]
    a = map(int, input().split())
    # lcm = 1
    # for n in a:
    #     lcm = (lcm*n)//gcd(lcm,n)
    def lcms(x, y):
        return (x * y) // gcd(x,y)
    lcm = reduce(lcms, a, 1)
    lcm //= 2
    print(M//lcm - M//(lcm*2))


if __name__ == "__main__":
    main()