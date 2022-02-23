from itertools import permutations

T = int(input())
full = 10**9*60*60*12
for case in range(T):
    A,B,C = map(lambda x: int(x), input().split())
    # print(A,B,C)
    for per in permutations([A,B,C]):
        nanosec = per[0] // 10**9
        sec = 720*10**9*nanosec
        min = 12*10**9*nanosec
        if tuple(per) == tuple(nanosec, min, sec):
            print("Case #"+str(case+1)+":",sec//(60*60),sec//60%60,nanosec,nanosec)

    # s = m = h = 0
    # for sec in range(12*60*60):
    #     # ss = sorted([s,m,h])
    #     SS = sorted([A,B,C])
    #     ans = False
    #     for per1 in permutations([s,m,h]):
    #         for n in range(2**3):
    #             num = bin(n)[2:]
    #             num = "0"*(3-len(num))+num
    #             tmp = [abs(per1[i]+SS[i]) if num[i] == "1" else abs(per1[i]-SS[i]) for i in range(3)]
    #             # if sec == 1800:
    #             #     print(per1, SS)
    #             #     print(num)
    #             #     print(tmp)
    #             if len(set(tmp)) == 1:
    #                 ans = True
    #                 break
    #         if ans:
    #             break
    #     if ans:
    #         # print(sec)
    #         # print(diff)
    #         print("Case #"+str(case+1)+":",sec//(60*60),sec//60%60,sec%60,0)
    #         break
    #     s = (s + 720*10**9) % full
    #     m = (m + 12*10**9) % full
    #     h = (h + 10**9) % full