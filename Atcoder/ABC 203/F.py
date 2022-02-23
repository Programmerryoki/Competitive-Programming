from bisect import bisect_right

def grasp(arr):
    count = 0
    high = len(arr)-1
    while -1 < high:
        count += 1
        h = arr[high] / 2
        high = bisect_right(arr, h)-1
    return count


N,K = map(int, input().split())
if N == K:
    print(0,K)
    exit()
A = [int(i) for i in input().split()]
A.sort()
total = 0
prev = grasp(A)
i = len(A)-1
while True:
    ga = grasp(A[:-1])
    if prev < ga or total == K:
        break
    elif prev == ga:
        while prev <= ga:
            ga = grasp(A[:i])
            
    A.pop()
    total += 1
    prev = ga
while True:
    ga = grasp(A[1:])
    if prev <= ga or total == K:
        break
    A = A[1:]
    total += 1
    prev = ga
print(grasp(A), total)