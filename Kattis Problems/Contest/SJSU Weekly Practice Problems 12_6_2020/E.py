from datetime import datetime, timedelta

ans = []
while True:
    n = int(input())
    if n == 0:
        break
    time = [input().split() for i in range(n)]
    time.sort(key= lambda x: datetime.strptime(x[0],"%H:%M") + (timedelta(hours=12) if x[1] == "p.m." else timedelta(0)) - (timedelta(hours=12) if x[0][:2]=="12" else timedelta(0)))
    ans.append(time)
print("\n\n".join(["\n".join([" ".join(i) for i in j]) for j in ans]))