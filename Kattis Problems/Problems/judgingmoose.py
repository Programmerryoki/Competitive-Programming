rt, lt = [int(i) for i in input().split()]
if [rt, lt] == [0, 0]:
    print("Not a moose")
else:
    print("Even", max(rt,lt) * 2) if rt == lt else print("Odd", max(rt, lt) * 2)