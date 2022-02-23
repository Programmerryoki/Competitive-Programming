from collections import Counter, deque

N = int(input())
S = input()
T = input()
CS = Counter(S)
CT = Counter(T)
if CS != CT:
    print(-1)
    exit()

def minn(S,T):
    check = "0" if CS["0"] < CS["1"] else "1"
    total = 0
    lst = deque()
    rev = False
    i = 0
    while i < N:
        # print()
        # print(S)
        # print(T)
        # print(lst)
        if T[i] == check:
            lst.append(i)
        if S[i] == check:
            try:
                index = lst.popleft()
                total += index != i
            except:
                # print("changing")
                lst.append(i)
                j = i
                while j < N:
                    if S[i] == check:
                        lst.append(j)
                    if T[i] == check:
                        try:
                            index = lst.popleft()
                        except:
                            break
                    j += 1
                S = S[:i] + S[i:j+1][::-1] + S[j+1:]
                T = T[:i] + T[i:j+1][::-1] + T[j+1:]
                # print(i,j)
                # print(total)
                lst.clear()
                i -= 1
        i += 1
    # print(total)
    return total

print(minn(S,T))
# print(min(minn(S,T), minn(S[::-1], T[::-1])))

# from collections import Counter, deque
#
# N = int(input())
# S = input()
# T = input()
# CS = Counter(S)
# CT = Counter(T)
# if CS != CT:
#     print(-1)
#     exit()
#
# def minn(S,T):
#     check = "0" if CS["0"] < CS["1"] else "1"
#     total = 0
#     lst = deque()
#     rev = False
#     i = 0
#     while i < N:
#         if T[i] == check:
#             lst.append(i)
#         if S[i] == check:
#             try:
#                 index = lst.popleft()
#                 total += index != i
#             except:
#                 check = "0" if check == "1" else "1"
#                 lst.append(i)
#                 rev = True
#         if rev and not lst:
#             rev = False
#             check = "0" if check == "1" else "1"
#         i += 1
#     return total
#
# print(min(minn(S,T), minn(S[::-1], T[::-1])))