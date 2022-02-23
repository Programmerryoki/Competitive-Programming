order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
code = input().split()
while len(code) != 1:
    shift = int(code[0])
    msg = list(code[1][::-1])
    for a in range(len(msg)):
        msg[a] = order[(order.index(msg[a]) + shift)%len(order)]
    print("".join(msg))
    code = input().split()