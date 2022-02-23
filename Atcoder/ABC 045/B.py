A = list(input())
B = list(input())
C = list(input())
pv = "abc"
p = 0
while True:
    if p == 0:
        if len(A) == 0:
            print("A")
            break
        p = pv.index(A.pop(0))
    elif p == 1:
        if len(B) == 0:
            print("B")
            break
        p = pv.index(B.pop(0))
    else:
        if len(C) == 0:
            print("C")
            break
        p = pv.index(C.pop(0))