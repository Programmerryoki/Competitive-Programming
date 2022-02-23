from collections import deque

T = int(input())
for case in range(T):
    S = input()
    position = {chr(ord("a")+i): deque() for i in range(26)}
    counter = [0]*26
    for i,s in enumerate(S):
        counter[ord(s)-ord("a")] += 1
        position[s].append(i)

    impos = False
    order = list(sorted([(counter[i], chr(ord("a")+i)) for i in range(len(counter))], reverse=True))
    search = [i[-1] for i in order]
    search = search[1:] + search[:1]
    ans = [""]*len(S)
    for i in range(len(order)):
        count, w = order[i]
        ind = 0
        for j in range(len(search)):
            if search[j] == w or not position[search[j]]:
                continue
            ind = j
            break

        for j in range(count):
            while not position[search[ind]]:
                ind += 1
            if search[ind] == w:
                impos = True
                break
            pos = position[search[ind]].popleft()
            ans[pos] = w
        if impos:
            break
    else:
        print("Case #"+str(case+1)+":","".join(ans))
        continue
    print("Case #"+str(case+1)+": IMPOSSIBLE")