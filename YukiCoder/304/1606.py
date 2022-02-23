N = int(input())
A = [int(i) for i in input().split()]
def minswap(A):
    i = 0
    j = len(A)-1
    total = 0
    while i < j:
        swap = False
        while i < len(A):
            if A[i] != 0:
                i += 1
                continue
            if (i > 0 and A[i-1] == 1) or (i < len(A)-1 and A[i+1] == 1):
                swap = True
                break
            i += 1
        while 0 <= j:
            if A[j] != 1:
                j -= 1
                continue
            if (j > 0 and A[j-1] == 0) or (j < len(A) and A[j+1] == 1):
                swap = True
                break
            j -= 1
        if i > j and swap == True:
            return -1
        if not swap:
            break
        total += 1
        A[i], A[j] = A[j], A[i]
    return total


print(minswap(list(A)), minswap(list(A[::-1])))