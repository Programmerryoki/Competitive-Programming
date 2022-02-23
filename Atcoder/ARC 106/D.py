def main():
    MOD = 998244353

    N,K = map(int, input().split())
    A = [int(i) for i in input().split()]
    ks = [0]*K

    for i in range(N-1):
        for j in range(i+1,N):
            n = A[i] + A[j]
            t = 1
            for k in range(K):
                t = (t * n) % MOD
                ks[k] = (ks[k] + t) % MOD
    print("\n".join(map(str, ks)))

if __name__ == "__main__":
    main()