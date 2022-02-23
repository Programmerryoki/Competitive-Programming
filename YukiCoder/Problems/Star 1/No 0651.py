a = int(input())
time = [10+a//100, int(a*60/100%60)]
if len(str(time[1])) == 1:
    time[1] = "0" + str(time[1])
print(":".join(map(str, time)))