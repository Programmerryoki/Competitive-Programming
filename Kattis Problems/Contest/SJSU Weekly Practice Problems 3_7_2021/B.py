def area(a,b,c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

N = int(input())
total = 0
for _ in range(N):
    A,B,C = map(int, input().split())
    m = (((A**2+B**2)/2) - (C/2)**2)**0.5
    area2 = area(A,B,C)/2
    total += ((area2 / m) * 4)
print(total)