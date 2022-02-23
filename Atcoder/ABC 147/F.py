# N, X, D = [int(i) for i in input().split()]
# seq = [X+i*D for i in range(N) if X+i*D != 0]
# n = len(seq)
# if n <= 3:
#     print(2**n)
# else:
#     print(X + (n**2+3*n-10)//2)

#
# from collections import deque
# add = [14 + i*20 for i in range(100)]
# a = [0]
# print(a)
# print(len(a))
# que = deque()
# for i in range(len(add)):
#     que.extend(a)
#     n = add[i]
#     a = []
#     while len(que) != 0:
#         j = que.popleft()
#         if j+n not in a:
#             a.append(j+n)
#         if j-n not in a:
#             a.append(j-n)
#     # print(a)
#     num = 2**i
#     print(i+1,len(a),num,num//14)
    # print(len(a), 2**(3+i+1),2**(3+i+1)-len(a) )
#
# print(1)
# print(2)
# print(4)
# print(8)
# t = 8
# for a in range(4,len(add)):
#     t = t + a + 1
#     print(t)

def mul(a,b):
    ans = [0 for i in range(len(a)+len(b)-1)]
    for i in range(len(b)):
        for j in range(len(a)):
            ans[i+j] += b[i]*a[j]
    return ans

# a = [1,0]
b = [1,0,0,0,1]
c = [1,0,0,0,0,0,1]
d = [1,0,0,0,0,0,0,0,1]
e = [1,0,0,0,0,0,0,0,0,0,1]
temp = mul(b,c)
temp = mul(temp, d)
temp = mul(temp, e)
print(temp)
print(len(temp) - temp.count(0))
# print(mul(mul(a,b),c))
temp = [1,1,1]
num = [1,1,1]
n = len(temp)
for a in range(n+1):
    temp = mul(temp,num)
    print(temp)
    print(len(temp),sum(temp))