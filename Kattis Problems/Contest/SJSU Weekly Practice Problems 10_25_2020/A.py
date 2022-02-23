from datetime import datetime

month = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
d,m = input().split()
d = int(d); m = month.index(m)+1
jf = input()
dow = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
jf = dow.index(jf)
try:
    dif0 = datetime(day=d, month=m, year=2001) - datetime(day=1,month=1,year=2001)
except:
    print("TGIF" if jf == 1 else ":(")
    exit()
dif1 = datetime(day=d, month=m, year=2000) - datetime(day=1,month=1,year=2000)
if dif0 == dif1:
    print(":(" if (dif0.days + jf) % 7 != 4 else "TGIF")
else:
    if (dif0.days + jf) % 7 == 4 or (dif1.days + jf) % 7 == 4:
        print("not sure")
    else:
        print(":(")