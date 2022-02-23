X = int(input())
m = 1
for b in range(1, int(X**0.5)+1):
    for p in range(2, X):
        if b**p <= X:
            m = max(m, b**p)
print(m)