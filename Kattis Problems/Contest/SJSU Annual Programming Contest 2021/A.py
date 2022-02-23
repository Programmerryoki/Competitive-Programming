C,X,M = map(float, input().split())
maxpos = 0
for _ in range(6):
    speed, fe = map(float, input().split())
    if C * fe * speed < 2 * X * M * fe + 2 * M * speed:
        continue
    maxpos = int(speed)
print("NO" if maxpos == 0 else "Yes "+str(maxpos))