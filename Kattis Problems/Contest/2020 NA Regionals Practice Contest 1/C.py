# T,K = map(int, input().split())
# t = [1]*T
# p = -1
# for throw in range(T-1):
#     for i in range(K):
#         try:
#             if p == T-1:
#                 p = t.index(1)
#             else:
#                 p = t.index(1, p+1)
#         except:
#             p = t.index(1)
#     t[p] = 0
# print(t.index(1))

m = 101
for T in range(1,m):
    for K in range(1,T+1):
        print(T,K,":",end=" ")
        t = [1]*T
        p = -1
        for throw in range(T-1):
            for i in range(K):
                try:
                    if p == T-1:
                        p = t.index(1)
                    else:
                        p = t.index(1, p+1)
                except:
                    p = t.index(1)
            print(p,end=" ")
            t[p] = 0
        # print(T,K,":",t.index(1))
        print("\tt:",t.index(1))
    print()
# for K in range(1,m):
#     print(" "*(len(str(m)) - len(str(K))) + str(K),end=" : ")
#     for T in range(1,m):
#         if T < K:
#             continue
#         t = [1]*T
#         p = -1
#         for throw in range(T-1):
#             for i in range(K):
#                 try:
#                     if p == T-1:
#                         p = t.index(1)
#                     else:
#                         p = t.index(1, p+1)
#                 except:
#                     p = t.index(1)
#             t[p] = 0
#         # print(T,K,":",t.index(1))
#         ind = t.index(1)
#         print(" "*(len(str(m)) - len(str(ind))) + str(ind), end=" ")
#     print()