S = input()
pre = ""
cur = ""
count = 0
for s in S:
    cur += s
    if pre != cur:
        count += 1
        pre = cur
        cur = ""
print(count)