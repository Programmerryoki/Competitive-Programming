dic = {}
while True:
    inp = input().split()
    if inp[0] == "0":
        break
    if "+" in inp:
        total = 0
        term = []
        for i in inp:
            if i == "+":
                continue
            try:
                total += int(i)
            except:
                if i in dic:
                    total += dic[i]
                else:
                    term.append(i)
        if total == 0 and len(term) > 0:
            print(" + ".join(term))
        else:
            print(total, end="")
            if len(term) > 0:
                print(" +", " + ".join(term))
            else:
                print()
    elif "=" in inp:
        dic[inp[0]] = int(inp[2])
    else:
        if inp[0] in dic:
            print(dic[inp[0]])
        else:
            print(inp[0])