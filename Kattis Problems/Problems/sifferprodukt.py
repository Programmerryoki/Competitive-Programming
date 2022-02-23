from functools import reduce

x = input()
while len(x) > 1:
    x = str(reduce(lambda x,y:x*y, [i for i in map(int, x) if i != 0]))
print(x)