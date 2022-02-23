T = int(input())
for case in range(T):
    S = input()
    check = list(set([int(i) for i in S]) - set([0]))
    check.sort()
    if len(check) == 0:
        print("Case #"+str(case+1)+": "+S)
        continue
    ma = check[-1]
    br = []
    for num in range(1,ma+1):
        # print(num)
        i = 0
        j = 0
        while i < len(S):
            # print(i,j)
            con = set([k for k in range(num)])
            # print(con)
            while j < len(S) and int(S[j]) not in con:
                j += 1
            if i != j:
                br.append([i, "("])
                br.append([j, ")"])
            while j < len(S) and int(S[j]) in con:
                j += 1
            i = j
            # print(br)
        # if i != j:
        #     br.append([i, "("])
        #     br.append([j-1, ")"])
    br.sort()
    br = br[::-1]
    # print(br)
    ans = list(S)
    for i, b in br:
        ans.insert(i, b)
    print("Case #"+str(case+1)+": "+"".join(ans))