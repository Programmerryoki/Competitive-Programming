N,M,K = [int(i) for i in input().split()]

def f(n, m):



"""
   n  0   1   2   3
m
0     0   1   2^K 3^K 4^K
1     0   1   1+2^K 1+2^K+3^K 1+2^K+3^K+4^K
2     0   1   2+2^K 3+2*2^K+3^K 4+3*2^K+2*3^K+4^K
3     0   1   3+2^K 6+2*2^K+3^K 10+5*2^K+3*3^K+4^K
4     0   1   4+2^K 10+2*2^K+3^K 20+7*2^K+4*3^K+4^K
5
"""