def main():
    N, t = [int(i) for i in input().split()]
    num = [int(i) for i in input().split()]
    if t == 1:
        nums = set(num)
        for n in nums:
            if 7777 - n in nums:
                print("Yes")
                break
        else:
            print("No")
    elif t == 2:
        if len(num) == len(set(num)):
            print("Unique")
        else:
            print("Contains duplicate")

    elif t == 3:
        dic = {}
        for n in num:
            try:
                dic[n] += 1
            except:
                dic[n] = 1
            if len(dic.keys()) > N//2+1:
                print(-1)
                break
        else:
            for i in dic.keys():
                if dic[i] > N//2:
                    print(i)
                    break
            else:
                print(-1)

    elif t == 4:
        num.sort()
        if N%2==0:
            print(num[N//2-1], num[N//2])
        else:
            print(num[N//2])

    elif t == 5:
        num.sort()
        i = 0
        while i < len(num) and num[i] < 100:
            i += 1
        j = i
        while j < len(num) and num[j] <= 999:
            j += 1
        print(" ".join(map(str, num[i:j])))

if __name__ == '__main__':
    main()