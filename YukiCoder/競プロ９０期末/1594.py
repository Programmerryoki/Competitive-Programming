from itertools import combinations

N = int(input())
E = [int(i) for i in input().split()]
se = set(E)
SE = sum(E)
if SE % 3 != 0:
    print("No")
    exit()

used = set()
def recur(cur, group):
    if group == 3:
        print("Yes")
        exit()
    for e in se - set(used):
        if e + cur < SE // 3:
            used.add(e)
            recur(cur + e, group)
            used.remove(e)
        elif e + cur == SE // 3:
            used.add(e)
            recur(0, group+1)
            used.remove(e)
        elif e + cur > SE // 3:
            return

recur(0, 0)
print("No")

# from itertools import permutations
#
# N = int(input())
# E = [int(i) for i in input().split()]
# se = sum(E)
# if se % 3 != 0:
#     print("No")
#     exit()
#
# def possible(arr):
#     cur = 0
#     count = 0
#     for i in arr:
#         if i + cur < se // 3:
#             cur += i
#         elif i + cur == se // 3:
#             cur = 0
#             count += 1
#         elif i + cur > se//3:
#             return False
#     return count == 3 and cur == 0
#
# for per in permutations(E, N):
#     if possible(per):
#         print("Yes")
#         exit()
# print("No")