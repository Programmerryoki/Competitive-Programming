from sys import stdin

# def main():
#     input = stdin.readline
#     prime = {2,3,5,7}
#     n,q = map(int,input().split())
#     num = 7
#     i = 4
#     while num <= n:
#         num += i
#         for p in prime:
#             if num%p==0:
#                 break
#         else:
#             prime.add(num)
#         i = 6 - i
#     print(len(prime))
#     ans = [0]*q
#     for i in range(q):
#         N = int(input())
#         if N in prime:
#             ans[i] = 1
#     print(*ans,sep="\n")
#
# if __name__ == "__main__":
#     main()