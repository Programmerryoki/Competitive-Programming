from fractions import gcd

def main():
    mod = 10**9 + 7

    N = int(input())
    A = input().split()
    AP = set(A)
    num = 1
    for n in AP:
        num = (num*int(n))//gcd(num,int(n))

    t = 0
    for n in A:
        t = (t + num//int(n))
    print(t%mod)


if __name__ == "__main__":
    main()
