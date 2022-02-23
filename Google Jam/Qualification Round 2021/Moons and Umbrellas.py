T = int(input())
for case in range(T):
    X,Y,S = input().split()
    X = int(X); Y = int(Y)
    LS = list(S)
    if LS.count("?") == len(LS):
        print("Case #"+str(case+1)+": 0")
        continue
    while LS.count("?"):
        for i in range(len(LS)):
            if LS[i] == "?":
                if i == 0:
                    if LS[i+1] != "?":
                        LS[i] = LS[i+1]
                elif i == len(LS)-1:
                    if LS[i-1] != "?":
                        LS[i] = LS[i-1]
                else:
                    if LS[i-1] == "?" and LS[i+1] == "?":
                        pass
                    elif LS[i-1] == "?":
                        LS[i] = LS[i+1]
                    elif LS[i+1] == "?":
                        LS[i] = LS[i-1]
                    else:
                        if LS[i-1] == LS[i+1]:
                            LS[i] = LS[i-1]
                        else:
                            LS[i] = "C"
    mcost = 0
    for i in range(len(LS)-1):
        if LS[i:i+2] == ["C","J"]:
            mcost += X
        elif LS[i:i+2] == ["J","C"]:
            mcost += Y
    print("Case #"+str(case+1)+":",mcost)