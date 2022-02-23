coord = [0,0,0]
for _ in range(4):
    x,y,z = map(int, input().split())
    coord = [(coord[0]+x)/2,(coord[1]+y)/2,(coord[2]+z)/2]
print(*coord)