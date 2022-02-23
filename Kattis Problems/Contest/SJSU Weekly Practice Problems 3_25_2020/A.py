n = int(input())
c = 0
for a in range(n):
    line = input().lower()
    if "pink" in line or "rose" in line:
        c += 1
if c != 0:
    print(c)
else:
    print("I must watch Star Wars with my daughter")