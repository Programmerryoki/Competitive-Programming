for a in range(2,100):
    print(a, pow(2,a-1,a))

# from collections import Counter
#
# def prime(n):
#     for a in range(2,int(n**0.5)+1):
#         if n%a==0:
#             return False
#     return True
#
# N = int(input())
# nums = [int(input()) for i in range(N)]
# Nums = Counter(nums)
# c = 0
# for a in Nums.keys():
#     if prime(a):
#         c += Nums[a]
# print(c)


# N = int(input())
# nums = [int(input()) for i in range(N)]
# m = max(nums)
# prime = [1]*(m+1)
# prime[0] = prime[1] = 0
# i = 0
# while True:
#     try:
#         i = prime.index(1,i+1)
#         for a in range(i*2,m+1,i):
#             prime[a] = 0
#     except:
#         break
#
# c = 0
# for a in nums:
#     if prime[a] == 1:
#         c += 1
# print(c)