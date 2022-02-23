from itertools import combinations, permutations

c1 = [int(i) for i in input().split()]
c2 = [int(i) for i in input().split()]
c3 = [int(i) for i in input().split()]
x = [i[0] for i in [c1,c2,c3]]
y = [i[1] for i in [c1,c2,c3]]
print(sum(set(x))*2 - sum(x), sum(set(y))*2 - sum(y))