T = int(input())
Ns = [int(input()) for i in range(T)]
mn = max(Ns)
calc = set(Ns)
ans = {}
arr = [0]*(mn+1)
arr[0] = 1
ele = 1
ans[1] = 1
for i in range(1,mn+1):
    arr[i] = 1
    for j in range(i-1,-1,-1):
        arr[j] = arr[j] * i + (arr[j-1] if j > 0 else 0)
    ele *= i+1
    if i+1 not in calc:
        continue
    total = 0
    for j in range(i+1):
        total += arr[j] * (j+1)
    ans[i+1] = total / ele
    print(arr)
for i,v in enumerate(Ns):
    print("Case #"+str(i+1)+":",ans[v])


# from itertools import permutations
#
# T = int(input())
# for case in range(T):
#     N = int(input())
#     tc = 0
#     tp = 0
#     for per in permutations([i for i in range(N)], N):
#         tp += 1
#         pn = -1
#         count = 0
#         for i in per:
#             if i > pn:
#                 pn = i
#                 count += 1
#         tc += count
#     print("Case #"+str(case+1)+":",tc / tp)