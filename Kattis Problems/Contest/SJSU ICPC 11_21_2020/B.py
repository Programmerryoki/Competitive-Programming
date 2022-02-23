n,t = map(int, input().split())
times = [[int(i) for i in input().split()] for j in range(n)]
td = sum([((times[(i+1)%n][0]-times[i][0])**2 + (times[(i+1)%n][1]-times[i][1])**2)**0.5 for i in range(n-1)])
gps = []
ct = 0; pos = tuple(times[0][:-1]); index = 0; tt = times[1][-1];dxt = (times[1][0] - pos[0]) / tt; dyt = (times[1][1] - pos[1]) / tt
for T in range(times[-1][-1]+1):
    # print(T,pos,ct,tt)
    if T < ct + tt:
        if T%t == 0:
            gps.append(pos)
    else:
        index += 1
        if index >= len(times)-1:
            gps.append(pos)
            break
        x,y,tt = times[index]; tt = (times[index+1][-1] - times[index][-1])
        dxt = (times[index+1][0] - pos[0]) / tt; dyt = (times[index+1][1] - pos[1]) / tt
        ct = times[index][-1]
    if T == times[-1][-1]:
        gps.append(pos)
    pos = (pos[0]+dxt, pos[1]+dyt)
# print(gps)
# print(td)
tgps = sum([((gps[i+1][0]-gps[i][0])**2 + (gps[i+1][1]-gps[i][1])**2)**0.5 for i in range(len(gps)-1)])
print((1 - (tgps / td)) * 100)