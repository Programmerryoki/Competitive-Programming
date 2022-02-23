a,b = [int(i) for i in input().split()]
c,d = [int(i) for i in input().split()]
t = int(input())
if abs(a-c) + abs(b-d) - t <= 0 and (abs(a-c) + abs(b-d) - t) % 2 == 0:
    print("Y")
else:
    print("N")