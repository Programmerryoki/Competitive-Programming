A,B,C = [int(i) for i in input().split()]
if A%2 == B%2 == C%2:
    m = max(A,B,C)
    print((3*m - A - B - C)//2)
elif A%2 == B%2:
    A += 1
    B += 1
    m = max(A,B,C)
    print(1 + (3*m - A - B - C)//2)
elif A%2 == C%2:
    A += 1
    C += 1
    m = max(A,B,C)
    print(1 + (3*m - A - B - C)//2)
elif B%2 == C%2:
    B += 1
    C += 1
    m = max(A,B,C)
    print(1 + (3*m - A - B - C)//2)