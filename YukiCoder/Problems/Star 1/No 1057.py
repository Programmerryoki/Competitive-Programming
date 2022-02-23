A,B = [int(i) for i in input().split()]
print(min(A,B)*2 if A != B else A*2-1)