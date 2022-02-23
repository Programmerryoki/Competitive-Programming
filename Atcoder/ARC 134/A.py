N,L,W = [int(i) for i in input().split()]
a = [-W]+[int(i) for i in input().split()]+[L]
no = 0
for i in range(len(a)-1):
    d = a[i+1] - (a[i] + W)
    no += -(-d//W)
print(no)