T = int(input())
for _ in range(T):
    N = int(input())
    N2 = N
    count = 0
    while N > 0:
        # print(N)
        SN = str(N)
        sub = ""
        left = 0
        i = 0
        zero = 0
        while i < len(SN):
            # print(i, SN, sub, left)
            left = int(str(left) + SN[i])
            if left < 1:
                zero = 1
                while 0 <= i-1 and int(sub[i-1]) - 1 == 0:
                    i -= 1
                if i == 0:
                    i = 1
                    sub = "3"
                    left = 7
                else:
                    sub = sub[:i-1] + str(int(sub[i-1])-1)
                    left = int(SN[:i] if SN[:i] else "0") - int(sub)
            elif left <= 3:
                sub += str(left)
                left = 0
                i += 1
                if zero:
                    zero = (zero+1) % 3
            else:
                if SN[i] in "234" and zero == 0:
                    sub += "1"
                    left -= 1
                else:
                    sub += "3"
                    left -= 3
                i += 1
                if zero:
                    zero = (zero+1) % 3
            if int(SN) == int(sub):
                break
            elif int(SN) < int(sub):
                sub = sub[:-1]
                break
        N -= int(sub)
        # print(sub, N)
        count += 1
    print(count)