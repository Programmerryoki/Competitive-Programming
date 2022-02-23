n, dm = [int(i) for i in input().split()]
d = [int(i) for i in input().split()]
c = 0
while c < len(d) and d[c] > dm:
    c += 1
if c == len(d):
    print("It had never snowed this early!")
else:
    print("It hadn't snowed this early in", c,"years!")