from math import log2, floor, ceil
from sys import stdin


def main():
    input = stdin.readline
    mul2 = [2]
    for i in range(7):
        mul2.append(mul2[-1]**2)
    mulp = [1]
    for i in range(13):
        mulp.append(mulp[-1]*2)
    for i in range(1,14):
        mulp[i] = mulp[i-1]+mulp[i]

    t = int(input())
    for _ in range(t):
        h, p = [int(i) for i in input().split()]
        n = floor(log2(p))
        if n+1 >= h:
            print(h)
            continue
        num = bin(max(0,h))[2:][::-1]
        total = 1
        for i in range(len(num)):
            if num[i] == "1":
                total *= mul2[i]
        total = max(0, total-1-mulp[n])
        print(min(n+1,h) + -(-total // p))


if __name__ == '__main__':
    main()