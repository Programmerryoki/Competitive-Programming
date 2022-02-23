from sys import stdin
from collections import defaultdict

def main():
    input = stdin.readline

    N,Q = map(int, input().split())
    classes = [int(i) for i in input().split()]
    stu = {i:defaultdict(set) for i in range(1,N+1)}
    for i in range(1,N+1):
        stu[i][classes[i-1]] = {i}
    # print(stu)
    ans = []
    for _ in range(Q):
        n,*rest = input().split()
        if n == "1":
            a,b = map(int, rest)
            ca = stu[a]; cb = stu[b]
            if len(ca) > len(cb):
                ca,cb = cb,ca
            for s in ca:
                cb[s] |= ca[s]
                for v in ca[s]:
                    stu[v] = cb
            # for s in cb:
            #     stu[s] = cb
            # for i in stu:
            #     print(stu[i])
            # print()
        else:
            x,y = map(int, rest)
            ans.append(len(stu[x][y]))

    print(*ans,sep="\n")

if __name__ == "__main__":
    main()