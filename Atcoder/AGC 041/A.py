N,A,B = [int(i) for i in input().split()]
if A%2 == B%2:
    print(abs(A - B) // 2)
    exit()

print(min((N - A + N - B + 1) // 2, (A + B - 1) // 2))