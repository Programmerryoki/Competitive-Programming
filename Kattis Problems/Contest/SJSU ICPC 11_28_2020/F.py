hp,wp,hm,wm = map(int, input().split())
paint = [input() for i in [0]*hp]
paints = [input() for i in [0]*hm]

hp,wp,hm,wm = [1,1,2000,2000]
paint = ["o"]
paints = ["o"*2000 for i in range(2000)]
print("start")

count = 0
for i in range(hm - hp + 1):
    for j in range(wm - wp + 1):
        suc = False
        for k in range(hp):
            for l in range(wp):
                # print(k,l,i+k,j+l)
                if paint[k][l] != paints[i+k][j+l]:
                    suc = True
                    break
            if suc:
                break
        else:
            count += 1
print(count)