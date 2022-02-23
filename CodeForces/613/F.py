from math import gcd

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort(reverse = True)
    k = 0
    ma = a[0]
    m = 0
    for i,nm in enumerate(a):
        num = nm*ma//gcd(nm, ma)
        if num > m:
            m = num
            k = i

    i = 1
    while i < k:
        ma = a[i]
        for j,nm in enumerate(a[:k]):
            num = nm*ma//gcd(nm, ma)
            if num > m:
                m = num
                k = j
        i += 1
    print(m)


if __name__ == "__main__":
    main()