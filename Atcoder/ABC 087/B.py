A = int(input())
B = int(input())
C = int(input())
X = int(input())
pos = {}
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            v = a*500 + b*100 + c*50
            pos.setdefault(v,0)
            pos[v] += 1
            if v > X:
                break
print(pos.setdefault(X,0))