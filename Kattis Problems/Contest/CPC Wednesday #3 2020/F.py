from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    inputs = input()[1:-1].split(",")
    x = deque()
    for a in inputs:
        try:
            int(a)
            x.append(a)
        except:
            break
    h = 0
    for s in p:
        if s == "R":
            h = 1 - h
        else:
            if len(x) == 0:
                print("error")
                break
            if h == 0:
                x.popleft()
            else:
                x.pop()
    else:
        if h == 0:
            print("["+",".join(map(str, x))+"]")
        else:
            print("["+",".join(map(str, list(x)[::-1]))+"]")