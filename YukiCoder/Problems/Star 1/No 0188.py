c = 0
month = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(1,len(month)+1):
    for j in range(1,month[i-1]+1):
        d = str(j) if len(str(j)) == 2 else "0"+str(j)
        if i == int(d[0]) + int(d[1]):
            c += 1
print(c)