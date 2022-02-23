from functools import reduce
N = int(input())
A = [int(i) for i in input().split()]
ans = [1 if a&1 else 2 for a in A]
print(3**N - reduce(lambda x,y: x*y, ans))