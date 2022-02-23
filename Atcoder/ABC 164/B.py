A,B,C,D = [int(i) for i in input().split()]
t = 0
while 0 < A and 0 < C:
    if t % 2 == 0:
        C -= B
    else:
        A -= D
    t += 1
if A <= 0:
    print("No")
else:
    print("Yes")