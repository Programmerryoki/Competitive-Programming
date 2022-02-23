while True:
    d = input()
    if d == "-":
        break
    m = int(input())
    for _ in range(m):
        h = int(input())
        d = d[h:] + d[:h]
    print(d)