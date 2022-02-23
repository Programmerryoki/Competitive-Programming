size = 7
arr = [i+1 for i in range(size)]
for a in range(2):
    for b in range(size):
        print(arr)
        n = size
        P = [int(i) for i in arr]
        ind = P.index(1)
        if ind == 0:
            if P[1] == n and n != 2:
                print(2)
            else:
                print(0)
        elif ind == n-1:
            if P[0] == n:
                print(1)
            else:
                print(min(3, ind))
        else:
            if P[ind-1] == n:
                print(min(ind, 1 + (n-ind) + 1))
            else:
                print(min(ind+2, 1 + (n-ind-1)))
        arr = arr[1:] + arr[:1]
    arr = arr[::-1]

# n = int(input())
# P = [int(i) for i in input().split()]
# ind = P.index(1)
# if ind == 0:
#     if P[1] == n and n != 2:
#         print(2)
#     else:
#         print(0)
# elif ind == n-1:
#     if P[0] == n:
#         print(1)
#     else:
#         print(min(3, ind))
# else:
#     if P[ind-1] == n:
#         print(min(ind, 1 + (n-ind) + 1))
#     else:
#         print(min(ind+2, 1 + (n-ind-1)))