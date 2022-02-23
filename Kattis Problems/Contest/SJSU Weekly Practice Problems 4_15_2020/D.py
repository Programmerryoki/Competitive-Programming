from math import ceil

P = int(input())
for _ in range(P):
    K, N = [int(i) for i in input().split()]
    arr = []
    for _ in range(ceil(N/10)):
        arr += [int(i) for i in input().split()]
    # print(arr)
    count = 0
    j = len(arr)-2
    m = 10**9+1
    while 0 <= j:
        # print(arr)
        # print(j,j+1,"->",arr[j],arr[j+1],count)
        if arr[j] > arr[j+1]:
            count += 1
            n = arr.pop(j)
            if n < m:
                m = n
        j -= 1
    i = len(arr)-1
    while i >= 0 and arr[i] > m:
        count += 1
        i -= 1
    # print(arr)
    # print(m)
    print(K,count)

# from math import ceil
#
# P = int(input())
# for _ in range(P):
#     K, N = [int(i) for i in input().split()]
#     arr = []
#     for _ in range(ceil(N/10)):
#         arr += [int(i) for i in input().split()]
#     print(arr)
#     count = 0
#     i = 0
#     j = 1
#     while i < len(arr) and j < len(arr):
#         print(i,j,"->",arr[i],arr[j],count)
#         if arr[i] <= arr[j]:
#             i += 1
#             j += 1
#         else:
#             j += 1
#             count += 1
#         # if i < len(arr) and j < len(arr):
#         #     print("",i,j,"->",arr[i],arr[j], count)
#     print(K,count)