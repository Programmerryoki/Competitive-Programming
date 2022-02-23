A,B,C = [int(i) for i in input().split()]
m = min(abs(A-B), abs(B-C), abs(C-A))
print(m)