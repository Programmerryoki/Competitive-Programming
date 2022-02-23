A,B,C = [int(i) for i in input().split()]
K = int(input())
c = 0
while B <= A:
    B *= 2
    c += 1
i = 1
while C <= B:
    C *= 2
    c += 1
if c <= K:
    print("Yes")
else:
    print("No")