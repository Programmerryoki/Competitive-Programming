N,A,B = [int(i) for i in input().split()]
print(max(0, (B*(N-1)+A) - (A*(N-1)+B) + 1))