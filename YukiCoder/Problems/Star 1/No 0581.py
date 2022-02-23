from functools import reduce
print(reduce(lambda x,y:x^y, [int(i) for i in input().split()]))