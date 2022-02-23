t = input().split(" ")
h = int(t[0])
m = int(t[1])
m -= 45
if m < 0:
    h -= 1
    m += 60
if h < 0:
    h = (h+24)%24
print(h,m)