T = int(input())
for a in range(T):
    n = [int(i) for i in input()]
    for i in range(len(n)):
        if i%2==1:
            index = len(n) - i - 1
            if len(str(n[index]*2)) < 2:
                n[index] = n[index] * 2
            else:
                n[index] = sum(map(int, list(str(n[index]*2))))
    if sum(n)%10 == 0:
        print("PASS")
    else:
        print("FAIL")