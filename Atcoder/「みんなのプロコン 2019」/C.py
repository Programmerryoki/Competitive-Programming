K,A,B = [int(i) for i in input().split()]
if A + 1 >= B or A >= K:
    print(K+1)
else:
    K += 1
    K -= A+2
    print(B + (K//2*(B-A)) + (K&1))