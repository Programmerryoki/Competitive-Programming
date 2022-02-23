t = int(input())
for a in range(t):
    n = ori = int(input())
    num = []
    for b in range(2,int(ori**0.5)+1):
        # print(n)
        if n % b == 0:
            num.append(b)
            n = n//b
            if len(num) == 2:
                if n != 1:
                    num.append(n)
                break
    num = list(set(num))
    if len(num) == 3:
        print("YES")
        print(" ".join(map(str, num)))
    else:
        print("NO")