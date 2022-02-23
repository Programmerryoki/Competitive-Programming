N,M,K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
i = 0
sa = 0
t = K
while i < len(A) and 0 < t:
    t -= A[i]
    if t < 0:
        break
    sa += 1
    i += 1
if 0 < t:
    i = 0
    while i < len(B) and 0 < t:
        t -= B[i]
        if t < 0:
            break
        sa += 1
        i += 1

i = 0
sb = 0
t = K
while i < len(B) and 0 < t:
    t -= B[i]
    if t < 0:
        break
    sb += 1
    i += 1
if 0 < t:
    i = 0
    while i < len(A) and 0 < t:
        t -= A[i]
        if t < 0:
            break
        sb += 1
        i += 1
print(max(sa,sb))

# i = j = 0
# book = 0
# time = K
# while i < len(A) or j < len(B):
#     if i < len(A) and j < len(B):
#         b = min(A[i], B[j])
#         if A[i] > B[j]:
#             j += 1
#         else:
#             i += 1
#     elif i < len(A):
#         b = A[i]
#         i += 1
#     elif j < len(B):
#         b = B[j]
#         j += 1
#     if K - b > 0:
#         book += 1
#         K -= b
#     elif K - b == 0:
#         book += 1
#         break
#     else:
#         break