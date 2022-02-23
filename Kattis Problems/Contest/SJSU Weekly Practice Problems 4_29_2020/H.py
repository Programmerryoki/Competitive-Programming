import math
n = int(input())
p = math.ceil(math.log(n, 9))
for i in range(p,0,-1):
    if n%(i**9) == 0:
        print(i)
        break