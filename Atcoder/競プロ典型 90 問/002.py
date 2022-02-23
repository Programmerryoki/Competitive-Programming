N = int(input())
if N&1:
    exit()
else:
    ans = []
    for n in range(2**N):
        num = bin(n)[2:]
        num = "0"*(N-len(num))+num
        i = 0
        for j in num:
            i += 1 if j == "0" else -1
            if i < 0:
                break
        else:
            if i == 0:
                ans.append("".join(["()"[int(i)] for i in num]))
    print("\n".join(ans))
    # l = [set() for i in range(N//2)]
    # l[0].add("()")
    # for index in range((N-2)//2):
    #     new = set()
    #     for p in l[index]:
    #         if len(p) < N:
    #             new.add("("+p+")")
    #         for i in range(2,N+1,2):
    #             if len(p) + i > N:
    #                 break
    #             for j in l[(i//2)-1]:
    #                 new.add(p+j)
    #                 new.add(j+p)
    #                 if len(p+j)+2 <= N:
    #                     new.add("("+p+j+")")
    #                     new.add("("+j+p+")")
    #     for i in new:
    #         l[(len(i)//2)-1].add(i)
    # print("\n".join(sorted(l[N//2-1])))