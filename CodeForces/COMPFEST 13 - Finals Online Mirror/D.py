s = input()
if s[-2:] in ["00","25","50","75"]:
    print(10**(s.count("_")-(s[0]=="_")) * 9**(s[0]=="_") * (10 - (1 if s[0]=="X" else 0) if "X" in s else 1))
elif s[-2:] == "XX":
    if len(s) == 2:
        print(0)
    else:
        print(10**(s.count("_")-(s[0]=="_")) * 9**(s[0]=="_") * (s[0] != "X"))
elif s[-2:] == "__":
    if len(s) == 2:
        print(3)
    else:
        print(4*10**(s.count("_")-(s[0]=="_")-2) * 9**(s[0]=="_") * (10 - (1 if s[0]=="X" else 0) if "X" in s else 1))
elif s[-2:] in ["X0", "X5"]:
    if len(s) == 2:
        print(1 if s[-1] == "0" else 2)
    elif s[-1] == "0":
        print(10**(s.count("_")-(s[0]=="_")) * 9**(s[0]=="_") * (2-(s[0]=="X") if "X" in s else 1))
    else:
        print(10**(s.count("_")-(s[0]=="_")) * 9**(s[0]=="_") * (2 if "X" in s else 1))
elif s[-2:] in ["0X","5X"]:
    if len(s) == 2:
        print(1)
    else:
        print(10**(s.count("_")-(s[0]=="_")) * 9**(s[0]=="_") * (s[0] != "X"))
elif s[-2:] in ["2X","7X"]:
    if len(s) == 2:
        print(1)
    else:
        print(10**(s.count("_")-(s[0]=="_")) * 9**(s[0]=="_"))
elif s[-2:] in ["_0","_5"]:
    if len(s) == 2:
        print(1 if s[-1] == "0" else 2)
    else:
        print(2*10**(s.count("_")-(s[0]=="_")-1) * 9**(s[0]=="_") * (10 - (1 if s[0]=="X" else 0) if "X" in s else 1))
elif s[-2:] in ["0_","5_","2_","7_"]:
    if len(s) == 2:
        print(1)
    else:
        print(10**(s.count("_")-(s[0]=="_")-1) * 9**(s[0]=="_") * (10 - (1 if s[0]=="X" else 0) if "X" in s else 1))
elif s[-2:] in ["X_"]:
    if len(s) == 2:
        print(3)
    else:
        print(10**(s.count("_")-(s[0]=="_")-1) * 9**(s[0]=="_") * (4 if s[0]!="X" else 3 if "X" in s else 1))
elif s[-2:] in ["_X"]:
    if len(s) == 2:
        print(3)
    else:
        print(2*10**(s.count("_")-(s[0]=="_")-1) * 9**(s[0]=="_") * (2 - (1 if s[0]=="X" else 0) if "X" in s else 1))
elif s == "0":
    print(1)
else:
    print(0)