n = int(input())

for a in range(n):
    up = int(input().split(" ")[-1])
    print(a+1,(1+up)*(up)//2,(up)**2,up**2+up)