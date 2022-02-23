A = input()
B = input()
i = 0
while i < len(A):
    if A[i] != B[i]:
        break
    i += 1
j = len(A)-1
while j > 0:
    if A[j] != B[j]:
        break
    j -= 1
j += 1
# print(i,j)
# print(A[i:j])
# print(B[i:j])
if A[i:j] != B[i:j][::-1]:
    print(0)
    exit()
i -= 1
count = 1
while i >= 0 and j < len(A):
    # print(A[i], A[j])
    if A[i] != A[j]:
        break
    i -= 1; j += 1
    count += 1
print(count)