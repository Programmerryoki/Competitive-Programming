key = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [-1,0,-1]
]
arr = [
    [1,4,7],
    [2,5,8,0],
    [3,6,9]
]

def pos(n):
    n = str(n)
    i = n[0]
    a = index(int(i))
    for j in n[1:]:
        b = index(int(j))
        # print(n, j, a, b)
        if a[0] <= b[0] and a[1] <= b[1]:
            a = b
        else:
            break
    else:
        return True
    return False


def index(n):
    index = [-1,-1]
    for i,a in enumerate(key):
        if n in a:
            index[0] = i
            break
    for j,a in enumerate(arr):
        if n in a:
            index[1] = j
            break
    return index

T = int(input())
for _ in range(T):
    k = int(input())
    p = k
    n = k
    while not pos(p):
        p += 1
    while not pos(n):
        n -= 1
    # print(p,n)
    if abs(k - p) > abs(k - n):
        print(n)
    else:
        print(p)