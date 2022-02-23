n = int(input())
sock = [int(i) for i in input().split()][::-1]
ap = [sock.pop()]
move = 1
while True:
    if len(sock) and not len(ap):
        ap.append(sock.pop())
    elif len(sock) and len(ap):
        if ap[-1] != sock[-1]:
            ap.append(sock.pop())
        else:
            ap.pop()
            sock.pop()
    elif len(sock) or len(ap):
        print("impossible")
        exit()
    else:
        print(move)
        exit()
    move += 1