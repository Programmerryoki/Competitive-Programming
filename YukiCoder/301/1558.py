from sys import stdin

def main():
    input = stdin.readline
    N,M,Q = [int(i) for i in input().split()]
    kukan = [[0]*N for i in range(M)]
    ans = []
    for _ in range(Q):
        # print(kukan)
        ty, *rest = [int(i)-1 for i in input().split()]
        if ty == 0:
            D, *P = rest
            kukan[D] = P
        elif ty == 1:
            S = rest[0]
            order = [i for i in range(N)]
            no = [0]*N
            for i in range(S+1):
                for j in range(N):
                    no[kukan[i][j]] = order[j]
                no,order = order, no
                # print(order)
            ans.append(" ".join([str(i+1) for i in order]))
        elif ty == 2:
            L,R = rest
            # print(L,R)
            order = list(kukan[L-1]) if L >= 1 else [i for i in range(N)]
            calc = list(order)
            # print(order)
            no = [0]*N
            for i in range(L, R+1):
                for j in range(N):
                    no[kukan[i][j]] = order[j]
                no,order = order, no
                # print(order)
            s = sum([abs(order[i] - calc[i]) for i in range(N)])
            ans.append(str(s))
    print("\n".join(ans))

if __name__ == '__main__':
    main()