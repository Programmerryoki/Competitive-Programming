N = int(input())
if N == 1:
    print(1)
    exit()
a = 2
b = 1
for i in range(1,N):
    a,b = b,a+b
print(b)