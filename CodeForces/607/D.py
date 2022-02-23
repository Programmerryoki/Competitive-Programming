t = int(input())
for a in range(t):
    r,c = [int(i) for i in input().split()]
    s = 0
    ans = 5
    h = [0 for i in range(c)]
    for b in range(r):
        line = input()
        i = 0
        for j in range(len(line)):
            if line[j] == "A":
                i += 1
                h[j] += 1
        s += i

        if ans > 4:
            if i >= 1:
                ans = 4
        if ans > 3:
            if line[0] == "A" or line[-1] == "A":
                ans = 3
            if b == 0 or b == r-1:
                if i >= 1:
                    ans = 3
        if ans > 2:
            if b == 0 or b == r-1:
                if line[0] == "A" or line[c-1] == "A":
                    ans = 2
            if i == c:
                ans = 2
        if ans > 1:
            if b == 0 or b == r-1:
                if i == c:
                    ans = 1

    if h[0] == r or h[-1] == r:
        ans = 1
    elif ans > 2 and r in h:
        ans = 2
    if s == r*c:
        print("0")
    elif ans > 4:
        print("MORTAL")
    else:
        print(ans)