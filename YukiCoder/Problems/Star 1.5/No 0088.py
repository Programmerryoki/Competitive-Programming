S = input()
c = 0
for _ in range(8):
    s = input()
    c += s.count("b") + s.count("w")
if not c&1:
    print(S)
else:
    if S == "oda":
        print("yukiko")
    else:
        print("oda")