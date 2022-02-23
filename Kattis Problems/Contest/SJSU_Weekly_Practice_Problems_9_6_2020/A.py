grid = [[int(i) for i in input().split()] for j in range(3)]
place = [0]*9
for i in range(3):
    for j in range(3):
        place[grid[i][j] - 1] = [i,j]
dis = 0
for i in range(len(place)-1):
    dis += ((place[i+1][0] - place[i][0])**2 + (place[i+1][1] - place[i][1])**2)**0.5
print(dis)