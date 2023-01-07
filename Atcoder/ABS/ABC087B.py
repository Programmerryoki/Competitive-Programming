A,B,C,X = [int(input()) for _ in range(4)]
tn = 0
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if i*500 + j*100 + k*50 == X:
                tn += 1
print(tn)