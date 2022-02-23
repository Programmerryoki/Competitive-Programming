import os
import time

front = []
back = []
p = ""


lines = str(os.read(0,1000000000)).split("\\n")
start_time = time.time()
n = int(lines[0][2])
lines = lines[1:-1]
for s in lines:
    #print(front, back)
    a = s.split(" ")
    com = a[0]
    x = (a[1])
    if com == "push_back":
        back.append(x)
    elif com == "push_front":
        front.append(x)
    elif com == "push_middle":
        if len(front) <= len(back):
            front.append(x)
        else:
            back.append(x)
    elif com == "get":
        n = int(x)
        if n < len(front):
            p += front[n] + "\n"
        else:
            p += back[n-len(front)] + "\n"
print(p)
# os.write(1, p)

print("%s seconds" % (time.time() - start_time))