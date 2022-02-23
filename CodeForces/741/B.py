from collections import Counter

check = "14689"

t = int(input())
for _ in range(t):
    k = int(input())
    n = input()
    sn = Counter(n)
    done = False
    for i in check:
        if i in sn:
            done = True
            print(1)
            print(i)
            break
    if done:
        continue
    if sn.most_common(1)[0][1] >= 2:
        print(2)
        print(sn.most_common(1)[0][0]*2)
        continue
    done = False
    for i in range(k-1, 0, -1):
        if n[i] == "2" or n[i] == "5":
            done = True
            # print("exx",n)
            print(i+1)
            print(n[:i+1])
            break
    if done:
        continue
    # print("ex:",n)
    m3 = [[] for i in range(3)]
    for i,v in enumerate(n):
        m3[int(v)%3].append((i,v))
    if len(m3[1])>0 and len(m3[2])>0:
        print(2)
        print("".join(i[1] for i in list(sorted([m3[1][0],m3[2][0]]))))
        continue
    for j in range(3):
        if len(m3[j]) > 2:
            print(3)
            print("".join(i[1] for i in list(sorted(m3[j][:3]))))
            break
    else:
        if len(m3[0]) > 1:
            print(2)
            print("".join(i[1] for i in list(sorted(m3[0][:2]))))
            continue
        raise ValueError