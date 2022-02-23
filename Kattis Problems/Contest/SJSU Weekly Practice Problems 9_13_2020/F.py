n1 = [int(i) for i in input()]
n2 = [int(i) for i in input()]
ans1 = ""
ans2 = ""

if len(n1) > len(n2):
    while len(n2) < len(n1):
        n2.insert(0,0)
else:
    while len(n2) > len(n1):
        n1.insert(0,0)

for a in range(len(n1)):
    if n1[a] > n2[a]:
        ans1 += str(n1[a])
    elif n1[a] < n2[a]:
        ans2 += str(n2[a])
    else:
        ans1 += str(n1[a])
        ans2 += str(n2[a])
if ans1 == "":
    print("YODA")
else:
    print(int(ans1))
if ans2 == "":
    print("YODA")
else:
    print(int(ans2))