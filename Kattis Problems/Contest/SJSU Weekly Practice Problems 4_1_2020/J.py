nums = [[],[],[1],[7],[4],[2,3,5],[0,6,9],[8]]
t = int(input())
for _ in range(t):
    n = int(input())
    print("\t",n)
    mi = ""
    temp = n
    while temp > 0:
        print(mi, temp)
        for i in range(7,1,-1):
            if i <= temp:
                if temp - i != 1:
                    mi += str(nums[i][0])
                    temp -= i
                else:
                    mi += str(nums[i-1][0])
                    temp -= (i-1)
    ma = ""
    temp = n
    while temp > 0:
        for i in range(2,8):
            if i <= temp:
                if temp - i != 1:
                    ma += str(nums[i][-1])
                    temp -= i
                else:
                    ma += str(nums[i-1][-1])
                    temp -= (i-1)
    print(mi,ma)