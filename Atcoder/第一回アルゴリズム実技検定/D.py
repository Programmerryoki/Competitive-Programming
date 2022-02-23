from functools import reduce

N = int(input())
A = [int(input()) for i in range(N)]
num = reduce(lambda x,y:x^y, [i for i in range(1,N+1)])
for a in A:
    num ^= a
if num == 0:
    print("Correct")
else:
    ma = max(A)
    if ma <= N:
        dif = ((N+1)*N)//2 - sum(set(A))
        print(num^dif, dif)
    else:
        print(num^ma, ma)