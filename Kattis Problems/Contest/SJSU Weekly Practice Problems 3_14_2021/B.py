Day = 1
answer = []
while True:
    try:
        input()
    except:
        break

    total = {}
    IN = {}
    while True:
        line = input()
        if line == "CLOSE":
            break
        cmd, name, time = line.split()
        time = int(time)
        if name in IN:
            if IN[name] != -1:
                if name in total:
                    total[name] += time - IN[name]
                else:
                    total[name] = time - IN[name]
                IN[name] = -1
            else:
                IN[name] = time
        else:
            IN[name] = time

    # print(total)
    cust = list(total.items())
    cust.sort()
    ans = "Day "+str(Day)+"\n"
    cus = []
    for i,(name, mon) in enumerate(cust):
        cus.append(name+" ${:.2f}".format(mon / 10))
    answer.append(ans+"\n".join(cus))
    Day += 1
print("\n\n".join(answer))