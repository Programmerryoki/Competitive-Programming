T = int(input())
for case in range(T):
    N,K = map(int, input().split())
    K = bin(K%(2**N))[2:]
    print("Case #"+str(case+1)+":","ON" if K.count("1") == len(K) and len(K) == N else "OFF")