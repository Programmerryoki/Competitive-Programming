S = input()
S1 = input()
if {S, S1} in [{"#.","#."}, {".#",".#"},{"..","##"},{"##",".."}]:
    print("Yes")
elif {S, S1} in [{"##","#."}, {"##",".#"},{".#","##"},{"#.","##"}]:
    print("Yes")
elif {S, S1} in [{"##","##"}]:
    print("Yes")
else:
    print("No")