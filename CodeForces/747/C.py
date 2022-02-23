t = int(input())
for _ in range(t):
    n,c = input().split()
    s = input()
    if len(set(s)) == 1 and s[0] == c:
        print(0)
    else:
        for i in range(len(s)//2,len(s)):
            if s[i] == c:
                print(1)
                print(i+1)
                break
        else:
            print(2)
            print(len(s)-1,len(s))