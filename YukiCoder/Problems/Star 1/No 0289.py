S = input()
t = 0
for i in S:
    try:
        t += int(i)
    except:
        continue
print(t)