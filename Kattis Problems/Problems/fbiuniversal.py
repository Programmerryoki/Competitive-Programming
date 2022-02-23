conv = "0123456789ACDEFHJKLMNPRTVWX"
cd = [2,4,5,7,8,10,11,13]

def CD(n):
    total = 0
    for i,a in enumerate(str(n)):
        total += cd[i]*conv.index(a)
    return conv[total%27]

def decimal(n):
    total = 0
    for i,a in enumerate(list(str(n))):
        total += int(conv.index(a))*27**(len(n)-i-1)
    return total

n = int(input())
for a in range(n):
    line = (input().split(" "))[1]
    check = CD(line[:-1])
    #print(check)
    if line[-1] != check:
        print(a+1,"Invalid")
    else:
        print(a+1,decimal(line[:-1]))