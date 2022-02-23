N,P = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
print(sum([1 for i in A if i < P]))