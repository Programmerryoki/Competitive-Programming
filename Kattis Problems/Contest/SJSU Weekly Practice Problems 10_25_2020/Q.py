import re

def getinput():
    codes = []
    while True:
        line = input()
        if line == "***END***":
            break
        if not re.fullmatch(r"\s+", line):
            codes.append(re.sub(r"\s+", " ", line.strip()))
    return codes


N = int(input())
match = [getinput() for i in range(N)]
ori = getinput()
ma = [0,""]
for file in match:
    fname = file[0]; file = file[1:]
    mm = 0
    # print(fname)
    for i in range(len(ori)):
        # print("\t",ori[i])
        try:
            j = file.index(ori[i])
            t = i
            while t < len(ori) and j < len(file) and ori[t] == file[j]:
                # print(ori[t], file[j])
                t += 1; j += 1
            if t < len(ori) and j < len(file):
                mm = max(mm, t - i)
            else:
                mm = max(mm, t-i-1)
        except:
            continue
    # print(mm, fname)
    if mm > ma[0]:
        ma = [mm, fname]
    elif mm == ma[0]:
        ma = [mm, ma[1] + " " + fname]
print(ma[0], ma[1]) if ma[0] != 0 else print(0)