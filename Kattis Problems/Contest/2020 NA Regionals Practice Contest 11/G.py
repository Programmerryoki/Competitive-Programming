from sys import stdin

def main():
    input = stdin.readline
    primes = {2}
    for n in range(3, 10**6):
        for p in primes:
            if n%p == 0:
                break
        else:
            primes.add(n)
    print(primes)

    Q = int(input())
    ans = [0]*Q
    for i in range(Q):
        n = int(input().strip())
        facf = []
        facb = []
        for fac in range(1,int(n**0.5)+1):
            if n % fac == 0:
                facf.append(fac)
                if n // fac != facf[-1]:
                    facb.append(n // fac)
        # print(facf+facb)
        count = 0
        for p in facf + facb:
            count += (not p in primes)
        ans[i] = count
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()