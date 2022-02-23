from random import randint

H = randint(2,10**5)
W = randint(2,10**5)
N = randint(3, min(H*W, 10**5))
points = [[randint(1,H),randint(1,W)] for i in range(N)]

print(H,W,N)
print("\n".join(" ".join(str(i) for i in j) for j in points))