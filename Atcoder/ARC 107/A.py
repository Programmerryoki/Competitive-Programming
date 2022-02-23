A,B,C = map(int, input().split())
s = lambda x: ((1+x)*x)//2
print((s(C)*s(B)*s(A)) % 998244353)