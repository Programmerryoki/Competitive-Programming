from sys import stdin


input = stdin.readline
M,S,T,L = [int(i) for i in input().split()]
TimePerStation = [[int(i) for i in input().split()] for j in range(M)]
StationCoord = [0]+[int(i) for i in input().split()]
DemandPerCar = [int(i) for i in input().split()]

StationDestination = [StationCoord[i]-StationCoord[i-1] for i in range(1,S+1)]

def DurationForCar(no):
    tt = 0
    waittime = 0
    for i in range(S):
        waittime += max(0, TimePerStation[no][i] - StationDestination[i])
        tt += max(TimePerStation[no][i], StationDestination[i])
    return tt, waittime, no


DurationPerCar = [DurationForCar(i) for i in range(M)]
# print(DurationPerCar)

order = sorted(DurationPerCar, key=lambda x: (-x[1], -x[0], x[2]))
ans = []
for i in range(len(order)):
    ans += [order[i][-1]+1] * DemandPerCar[i]
print(sum(DemandPerCar))
print(" ".join(str(i) for i in ans))