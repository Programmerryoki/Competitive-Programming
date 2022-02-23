d = 0
s = 0
t = [0,0,0]
dp = lambda p,c:((c[0]*3600+c[1]*60+c[2]) - (p[0]*3600+p[1]*60+p[2]))
distance = lambda p,c,s: (dp(p,c)*s)/3600
while True:
    try:
        line = input().split()
    except:
        break

    if len(line) == 1:
        time = list(map(int, line[0].split(":")))
        print(line[0],"{:.2f}".format(round(distance(t,time,s) + d, 2)), "km")
    else:
        time = list(map(int, line[0].split(":")))
        # print(t, time, s, distance(t, time, s), dp(t,time))
        d += distance(t,time,s)
        t = time
        s = int(line[1])
        # print(t, d, s)