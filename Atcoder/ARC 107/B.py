N,K = map(int, input().split())
total = 0
for A in range(2*N, 2, -1):
    B = A-K
    print(A,B,total)
    total += max(A-2*N+1,0) * max(B-2*N+1,0)
print(total)

# N,K = map(int, input().split())
# total = 0
# for A in range(2*N, 2, -1):
#     B = A-K
#     # print(A,B)
#     for a in range(min(N,A), 0, -1):
#         b = A-a
#         # print("\t",a,b)
#         if not (1 <= b <= N):
#             break
#         for c in range(min(N,B-1), 0, -1):
#             d = B-c
#             # print("\t\t",c,d)
#             if not (1 <= d <= N):
#                 break
#             total += 1
# print(total)