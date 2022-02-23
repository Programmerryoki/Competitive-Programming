n = int(input())
t = 1
while n != 0:
    count = 0
    save = []
    c = n
    print("SET",t)
    for a in range(n):
        s = input()
        if count % 2 == 0:
            print(s)
        else:
            save.insert(0,s)
        count += 1;
    for a in save:
        print(a)
    t += 1
    n = int(input())