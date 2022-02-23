from collections import Counter

S = input()
if len(S) < 3:
    if int(S) % 8 == 0:
        print("Yes")
    elif int(S[::-1]) %8 == 0:
        print("Yes")
    else:
        print("No")
    exit()
ss = Counter(S)
for i in range(13,125):
    n = str(i*8)
    cn = Counter(n)
    # print(n, cn, cn-ss)
    if len(cn-ss) == 0:
        print("Yes")
        exit()
print("No")