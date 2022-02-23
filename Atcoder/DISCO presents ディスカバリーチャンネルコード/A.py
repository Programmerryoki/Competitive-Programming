x, y = [int(i) for i in input().split()]
mon = 0
money = [300000, 200000, 100000]
if x -1 < 3:
    mon += money[x-1]
if y -1 < 3:
    mon += money[y-1]
if x == y and x == 1:
    mon += 400000
print(mon)