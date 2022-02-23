w = input()
count = {}
for s in w:
    try:
        count[s] += 1
    except:
        count[s] = 1
for s in count.values():
    if s&1:
        print("No")
        break
else:
    print("Yes")