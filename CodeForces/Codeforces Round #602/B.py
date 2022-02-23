from collections import Counter

t = int(input())
for a in range(t):
    n = int(input())
    q = [int(i) for i in input().split()]
    qn = Counter(q)
    qa = q.copy()
    miss = [i for i in range(1,len(q)+1) if i not in qn]
    if len(miss) == 0:
        print(" ".join(map(str, q)))
    else:
        ma = q[0]
        pos = True
        i = 0
        for a in range(len(q)):
            ma = max(ma, qa[a])
            # print(ma)

            if qn.get(q[a]) > 1:
                if miss[i] < ma:
                    qa[qa.index(q[a],a+1)] = miss[i]
                else:
                    pos = False
                    break
                i += 1
                qn[q[a]] -= 1

        if pos:
            print(" ".join(map(str, qa)))
        else:
            print(-1)