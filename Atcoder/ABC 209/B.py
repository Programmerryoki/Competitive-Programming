N,X = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
print("Yes" if sum(A) - (N//2) <= X else "No")