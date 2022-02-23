T = [int(i) for i in input().split(":")]
T[1] += 5
T[0], T[1] = str((T[1]//60 + T[0])%24), str(T[1]%60)
if len(T[0]) == 1:
    T[0] = "0" + T[0]
if len(T[1]) == 1:
    T[1] = "0" + T[1]
print(":".join(T))