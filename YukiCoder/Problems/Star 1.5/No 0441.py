A,B = input().split()
if A == "0" and B == "0":
    print("E")
elif A == "2" and B == "2":
    print("E")
elif A in {"0", "1"} or B in {"0", "1"}:
    print("S")
else:
    print("P")