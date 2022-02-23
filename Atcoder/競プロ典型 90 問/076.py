N = int(input())
A = [int(i) for i in input().split()]
SA = sum(A)
if SA % 10 != 0:
    print("No")
    exit()
A = A + A
j = 0
cur = 0
for i in range(len(A)):
    if cur + A[i] < SA // 10:
        cur += A[i]
    elif cur + A[i] == SA // 10:
        print("Yes")
        exit()
    else:
        while cur + A[i] > SA // 10:
            cur -= A[j]
            j += 1
        if cur + A[i] == SA // 10:
            print("Yes")
            exit()
        cur += A[i]
print("No")