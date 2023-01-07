N = int(input())
a = [int(i)for i in input().split()]
a.sort(reverse=True)
A,B = 0,0
for i,n in enumerate(a):
    if i&1:
        B += n
    else:
        A += n
print(A - B)