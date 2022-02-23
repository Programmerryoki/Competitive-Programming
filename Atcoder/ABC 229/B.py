A, B = [i[::-1] for i in input().split()]
for i in range(min(len(A), len(B))):
    if int(A[i]) + int(B[i]) >= 10:
        print("Hard")
        exit()
print("Easy")