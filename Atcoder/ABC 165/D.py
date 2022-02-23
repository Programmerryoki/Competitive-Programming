A,B,N = [int(i) for i in input().split()]
x = min(B-1, N)
print(int(A * x / B) - A * int(x / B))


# A,B,N = [int(i) for i in input().split()]
# x = min(B, N)
# floor = lambda A,B,x: (A*x)//B - A*(x//B)
# prev = floor(A,B,x)
# s = A//B
# while True:
#     x -= 1
#     c = floor(A,B,x)
#     if prev <= c:
#         prev = c
#     else:
#         break
# print(prev)