N = int(input())
A = [int(i) for i in input().split()]
m2 = 0
m4 = 0
for a in A:
    m2 += int(a%2 == 0 and not a%4 == 0)
    m4 += int(a%4 == 0)
if m4 >= N//2:
    print("Yes")
elif m4*2 + m2 >= N:
    print("Yes")
else:
    print("No")