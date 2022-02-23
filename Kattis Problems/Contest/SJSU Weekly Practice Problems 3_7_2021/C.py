case = 1
while True:
    line = input()
    if line == "END":
        break
    even = True
    if len(line) == 1:
        pass
    elif len(line) == line.count("*"):
        pass
    else:
        pat = []
        line = line[1:]
        while line:
            index = line.index("*")
            pat.append(index)
            line = line[index+1:]
        if line:
            even = False
        if pat.count(pat[0]) != len(pat):
            even = False

    print(case,"EVEN" if even else "NOT EVEN")
    case += 1