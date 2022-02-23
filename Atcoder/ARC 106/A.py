from math import log, ceil

N = int(input())
for A in range(1,ceil(log(N, 3))+1):
    for B in range(1,ceil(log(N, 5))+1):
        if 3**A + 5**B == N:
            print(A,B)
            exit()
print(-1)

# from math import log
#
# N = int(input())
# B = 1
# nb = 5
# while nb < N:
#     num = log(N - nb, 3)
#     if num.is_integer() and round(num) > 0:
#         if log(N-(3**int(num)), 5).is_integer():
#             print(int(num), B)
#             exit()
#     B += 1
#     nb *= 5
# print(-1)