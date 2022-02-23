n = int(input())
str = input()
if n%2==1:
    print(-1)
else:
    arr = [-1 if i == ")" else 1 for i in str]
    # print(arr)
    if sum(arr) != 0:
        print(-1)
    else:
        c = 0
        i = -1
        tc = 0
        for j,a in enumerate(arr):
            c += a
            if c == 0:
                if a > 0:
                    tc += j - i
                i = j
            # print(a,c,tc,i)
        print(tc)