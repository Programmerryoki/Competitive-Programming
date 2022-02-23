while True:
    n = input()
    if n.split()[1] == "?":
        break
    print(int(eval(n)))