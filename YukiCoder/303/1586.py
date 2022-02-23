N = int(input())
A = [int(i) for i in input().split()]
print("Yes" if (sum(A) % N == 0) else "No")