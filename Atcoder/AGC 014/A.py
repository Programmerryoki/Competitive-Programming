A,B,C = [int(i) for i in input().split()]
if A == B == C and not A&1:
    print(-1)
    exit()
c = 0
while not (A&1 or B&1 or C&1):
    A,B,C = (B+C)//2, (A+C)//2, (A+B)//2
    c += 1
print(c)