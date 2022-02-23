N = int(input())
for _ in range(N):
    msg = input()
    M = 0
    while (M)**2 < len(msg):
        M += 1
    msg += "*"*(M**2 - len(msg))
    smsg = [msg[i*M:i*M+M] for i in range(M)]
    emsg = "".join(["".join([smsg[j][i] for j in range(M-1,-1,-1)]) for i in range(M)])
    print(emsg.replace("*", ""))