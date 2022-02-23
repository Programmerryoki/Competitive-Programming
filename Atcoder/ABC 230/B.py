S = input()
if len(S) == 1:
    print("Yes")
    exit()
cycle = ["o","x","x"]
d = 0
if S[0] == "o" and S[1] == "x":
    d = 0
elif S[0] == "x" and S[1] == "x":
    d = 1
elif S[0] == "x" and S[1] == "o":
    d = 2
S = "".join(cycle[:d]) + S
t = -(-len(S)//3)
if S == ("oxx"*t)[:len(S)]:
    print("Yes")
else:
    print("No")