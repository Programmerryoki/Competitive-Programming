from itertools import permutations

S1 = input()
S2 = input()
SS2 = list(set(S2))
S3 = input()
SS3 = list(set(S3))
if len(set(S1) | set(S2) | set(S3)) > 10:
    print("UNSOLVABLE")
    exit()

toten = [i for i in range(10)]
for per in permutations(toten, len(SS3)):
    dic = {SS3[i]:per[i] for i in range(len(SS3))}
    rdic = {}
    ok = True
    for key,val in dic.items():
        if val in rdic:
            ok = False
            break
        rdic[val] = key
    if not ok:
        continue
    dic = {**dic, **rdic}
    if (len(S3) != 1 and dic[S3[0]] == 0) or (len(S3) == 1 and dic[S3[0]] == 0):
        continue
    print(per)
    for perm in permutations(toten, len(SS2)):
        dic2 = {SS2[i]:perm[i] for i in range(len(SS2))}
        rdic2 = {}
        ok = True
        for key,val in dic2.items():
            if val in rdic2:
                ok = False
                break
            rdic2[val] = key
        if not ok:
            continue
        dic2 = {**dic2, **rdic2}
        # print(dic, dic2)
        if (len(S2) != 1 and dic2[S2[0]] == 0) or (len(S2) == 1 and dic2[S2[0]] == 0):
            continue
        ok = True
        for key, val in dic2.items():
            # print(key, val)
            if key in dic:
                if val != dic[key]:
                    ok = False
                    break
            elif val in dic:
                ok = False
                break
        if not ok:
            continue

        is3 = int("".join([str(dic[i]) for i in S3]))
        is2 = int("".join([str(dic2[i]) for i in S2]))
        if is3 < is2:
            continue
        s1 = is3 - is2
        if len(str(s1)) != len(S1):
            continue
        ils1 = [int(i) for i in str(s1)]
        dicor = {**dic, **dic2}
        ok = True
        # print(s1, dicor)
        for i,key in enumerate(S1):
            if key in dicor:
                if dicor[key] != int(str(s1)[i]):
                    ok = False
                    break
            elif ils1[i] in dicor:
                ok = False
                break
        if not ok:
            continue
        print(s1)
        print(is2)
        print(is3)
        exit()
print("UNSOLVABLE")

# from sys import setrecursionlimit
# setrecursionlimit(10**8)
#
# from itertools import permutations
#
# SS = [input() for i in range(3)]
# if min(len(SS[0]),len(SS[1])) > len(SS[2]):
#     print("UNSOLVABLE")
#     exit()
# ans = []
#
#
# def check(index, nums):
#     return (int(nums[0][index]) + int(nums[1][index])) % 10 != int(nums[2][index])
#
#
# def cs(index, nums):
#     return int((int(nums[0][index]) + int(nums[1][index])) // 10)
#
#
# def dfs(dic: dict, index: int, rems: int):
#     s = [SS[i][index] for i in range(3)]
#     if s[0] in dic and s[1] in dic and s[2] in dic:
#         s2 = dic[s[0]] + dic[s[1]]
#         if s2%10 != dic[s[2]]:
#             return
#         dfs(dic, index, int(s2//10))
#         return
#     elif s[0] in dic and s[1] in dic:
#         s2 = dic[s[0]] + dic[s[1]]
#         dfs(dic, index, int(s2//10))
#         return
#     elif (s[0] in dic or s[1] in dic) and s[2] in dic:
#         if dic[s[0]] > dic[s[2]]:
#             dif = dic[s[0]] - dic[s[2]]
#
#             dfs()
#         elif dic[s[0]] == dic[s[2]]:
#         else:
#
#     ss = list(set(s[:-1]))
#     newd = {}
#     for per in permutations([i for i in range(10)], len(ss)):
#         for i,val in enumerate(ss):
#             newd[ss[i]] = val
#
# dfs({},0,0,[0]*3,0)