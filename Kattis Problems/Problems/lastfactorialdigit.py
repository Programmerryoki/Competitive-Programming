n = int(input())
for a in range(n):
    num = int(input())
    if num >= 5:
        print("0")
    else:
        total = 1
        for b in range(1,num+1):
            total = total*b%10
        print(total)