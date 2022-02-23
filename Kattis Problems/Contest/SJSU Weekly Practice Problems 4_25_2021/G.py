T = int(input())
for case in range(T):
    N,K = map(int, input().split())
    mod = 2**N
    print("Case #"+str(case+1)+":","OFF" if (K + 1) % mod != 0 else "ON")