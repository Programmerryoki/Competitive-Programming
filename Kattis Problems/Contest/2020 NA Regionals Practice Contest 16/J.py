s = input()
ls = len(s)
carry = False
while True:
    twos = 0
    ns = [""]*ls
    for i in range(ls):
        if int(s[i]) >= 2:
            ns[i] = str(int(s[i])-2+carry)
            if int(ns[i]) >= 2:
                twos += 1
            if i == 0:
                carry = True
            else:
                carry = (i != ls-1)
                si = int(ns[i-1])
                if si == 1:
                    twos += 1
                ns[i-1] = str(si+1)
        else:
            ns[i] = str(int(s[i]) + carry)
            if int(ns[i]) >= 2:
                twos += 1
            carry = False
    # print(twos,ns)
    if twos:
        s = ns
        continue
    else:
        print("".join(ns))
        break