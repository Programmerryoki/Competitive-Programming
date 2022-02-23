import sys, os
import time

tque = []
# p = bytearray()
p = ""
c = 0

# n = int(sys.stdin.readline())
lines = str(os.read(0,1000000000000000000)).split("\\n")
start_time = time.time()
n = int(lines[0][2])
lines = lines[1:-1]
#print(lines)
for s in lines:
    #print(tque)
    a = s.split(" ")
    com = a[0]
    x = (a[1])
    if com == "push_back":
        tque.append(x)
        c += 1
    elif com == "push_front":
        tque.insert(0,x)
        c += 1
    elif com == "push_middle":
        tque.insert((c + 1)//2,x)
        c += 1
    elif com == "get":
        # sys.stdout.write(str(tque[x])+"\n")
        p += tque[int(x)] + "\n"
print(tque)
print(p)
print("%s seconds" % (time.time() - start_time))
#os.write(0, p)