dis = []
for a in range(10):
    mod = int(input())%42
    if mod not in dis:
        dis.append(mod)
print(len(dis))