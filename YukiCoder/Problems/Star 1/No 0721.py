dates = [int(i) for i in input().split("/")]
months = [31,28,31,30,31,30,31,31,30,31,30,31]
if dates[0]%4==0 and (dates[0]%100 != 0 or dates[0]%400==0):
    months[1] = 29
dates[2] += 2
if dates[2] > months[dates[1] - 1]:
    dates[1], dates[2] = dates[1] + dates[2]//months[dates[1] - 1], dates[2] - months[dates[1] - 1]
if dates[1] > 12:
    dates[1] = dates[1] - 12
    dates[0] += 1
dates = [str(i) if len(str(i)) >= 2 else "0"+str(i) for i in dates]
print("/".join(dates))