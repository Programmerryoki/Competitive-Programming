n = int(input())
for _ in range(n):
    s = input()
    for i in range(1,len(s)+1):
        # print((s[:i]*(-(-len(s)//i))))
        if (s[:i]*(-(-len(s)//i)))[:len(s)] == s:
            print(i)
            break