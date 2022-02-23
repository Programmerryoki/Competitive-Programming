flag = [int(i) for i in input().split()]
if flag[-1] or flag[:-1].count(1) < 2:
    print("SURVIVED")
else:
    print("DEAD")