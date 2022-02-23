import sys
sys.setrecursionlimit(2000)

S = input()
pos = False
add = ["dream", "dreamer", "erase", "eraser"]
def recur(T):
    global pos
    if T == S:
        pos = True
        return
    for a in add:
        if len(T + a) <= len(S):
            recur(T + a)
recur("")
if pos:
    print("YES")
else:
    print("NO")