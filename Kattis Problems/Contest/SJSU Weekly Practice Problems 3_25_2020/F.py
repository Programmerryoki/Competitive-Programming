names = []
while True:
    try:
        names.append(input().split()[::-1])
    except:
        break
names.sort()
fn = [i[1] for i in names]
for i,n in enumerate(fn):
    if fn.count(n) > 1:
        j = i
        while j < len(fn):
            fn[j] = names[j][1] + " " + names[j][0]
            try:
                j = fn.index(n,j+1)
            except:
                break
print("\n".join(fn))