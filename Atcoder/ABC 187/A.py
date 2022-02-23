A,B = [int(i) for i in input().split()]
print(max(sum(int(i) for i in str(A)), sum(int(i) for i in str(B))))