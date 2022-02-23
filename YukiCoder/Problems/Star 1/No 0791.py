n = input()
if n[0] != "1":
    print(-1)
else:
    n = list(n[1:])
    if n.count("3") != len(n) or len(n) <= 0:
        print(-1)
    else:
        print(len(n))