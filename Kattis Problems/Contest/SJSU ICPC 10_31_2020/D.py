import heapq
from sys import stdin
from bisect import bisect_left, insort_left

def main():
    input = stdin.readline
    N = int(input())
    clinic = [[] for i in [0]*101]
    names = {}
    ans = []
    for i in range(N):
        n, *r = input().split()
        # print(n,r)
        if n == "0":
            cn, il = r
            ci = [-int(il), i, cn]
            # heapq.heappush(clinic, ci)
            ind = int(il)
            # index = bisect_left(clinic[ind],ci)
            # cind = clinic[ind]
            # cind.append([])
            # for i in range(len(cind)-1,index,-1):
            #     cind[i] = cind[i-1]
            # cind[index] = ci
            insort_left(clinic[ind], ci)
            names[cn] = ci
        elif n == "1":
            cn, ii = r
            pl = (-names[cn][0])
            names[cn][0] -= int(ii)
            nl = (-names[cn][0])
            if pl == nl:
                clinic[nl].sort()
                # heapq.heapify(clinic[nl])
            else:
                clinic[pl].remove(names[cn])
                insort_left(clinic[nl], names[cn])
            # clinic.sort()
        elif n == "2":
            [cn] = r
            clinic[(-names[cn][0])].remove(names[cn])
            del names[cn]
        elif n == "3":
            for j in range(100,-1,-1):
                if clinic[j]:
                    for [il,i,cn] in clinic[j]:
                        if cn in names:
                            ans.append(cn)
                            break
                    else:
                        continue
                    break
            else:
                ans.append("The clinic is empty")

        # print(clinic)
        # print(names)
    print(*ans, sep="\n")

if __name__ == "__main__":
    main()