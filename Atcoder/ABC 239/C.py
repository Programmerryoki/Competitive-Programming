x1,y1,x2,y2 = [int(i) for i in input().split()]
moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
xy1 = set([(x1+dx, y1+dy) for dx,dy in moves])
xy2 = set([(x2+dx, y2+dy) for dx,dy in moves])
print("Yes" if xy1 & xy2 else "No")