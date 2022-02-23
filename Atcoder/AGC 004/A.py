side = [int(i) for i in input().split()]
side.sort()
print(side[0]*side[1] if side[2]&1 else 0)