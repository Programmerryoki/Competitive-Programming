n = int(input())
t = 0
num = 2
while num <= n:
    t += n//num
    num *= 2

for i in range(3,n+1):
    if i%2 and pow(2,i-1,i)==1:
        num = i
        while num <= n:
            t += n//num
            num *= i
print(t)

# n = int(input())
# prime = [1]*(n+1)
# prime[0] = 0
# prime[1] = 0
# t = 0
# i = 0
# while True:
#     try:
#         i = prime.index(1,i+1)
#         for a in range(i*2,n+1,i):
#             prime[a] = 0
#         num = i
#         while num <= n:
#             t += n//num
#             num *= i
#     except:
#         break
# print([i for i in range(n+1)])
# print(prime)
# print(t)