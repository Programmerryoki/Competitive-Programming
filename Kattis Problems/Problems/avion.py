ans = []
for a in range(1,6):
    blimp = input()
    if "FBI" in blimp:
        ans.append(a)
    """for b in range(len(blimp)-2):
        print(blimp[b:b+3])
        if "FBI" == blimp[b:b+3]:
           ans.append(a)"""
if len(ans) == 0:
    print("HE GOT AWAY!")
else:
    print(" ".join(list(map(str, ans))))