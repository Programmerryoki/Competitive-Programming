for n in range(9877, 999, -1):
    ns = str(n) + str(n*2)
    if len(ns) == 9 and len(set(ns)) == 9 and '0' not in ns:
        print(ns)