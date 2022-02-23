N, K = [int(i) for i in input().split()]
d = [int(i) for i in input().split()]
D = [1 if i not in d else 0 for i in range(10)]
for a in range(N,10*N+1):
    for b in str(a):
        if D[int(b)] == 0:
            break
    else:
        print(a)
        break

# N, K = [int(i) for i in input().split()]
# dl = [int(i) for i in input().split()]
# D = [1 if i not in dl else 0 for i in range(10)]
# D = D + D[:1]
# n = str(N)[::-1]
# ans = []
# add = 0
# for a in range(len(n)):
#     try:
#         num = D.index(1, int(n[a])+add)
#         ans.append(num%10)
#         if num == 10:
#             add = 1
#         else:
#             add = 0
#     except:
#         add = 1
#         ans.append(D.index(1))
# if add == 1:
#     ans.append(D.index(1,add))
# # print(D)
# print("".join(map(str, ans[::-1])))