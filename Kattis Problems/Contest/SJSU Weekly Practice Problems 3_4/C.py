N, b = [int(i) for i in input().split()]
if N <= 2**(b+1)-1:
    print("yes")
else:
    print("no")