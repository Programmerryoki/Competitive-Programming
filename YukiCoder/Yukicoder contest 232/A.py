s = input().split(",")
suc = True
for a in s:
    if a in ["WA","TLE","MLE"]:
        suc = False
if suc:
    print("Done!")
else:
    print("Failed...")