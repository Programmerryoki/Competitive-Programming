A = [int(i) for i in input().split()]
if len(set(A)) == len(A) and (A[1] == max(A) or A[1] == min(A)):
    print("INF")
else:
    c = 0
    for i in range(max(A), 0, -1):
        B = [j%i for j in A]
        if len(set(B)) == len(B) and (B[1] == max(B) or B[1] == min(B)):
            c += 1
    print(c)