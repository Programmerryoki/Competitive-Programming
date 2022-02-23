n = int(input())
a = [int(i) for i in input().split()]
for i in range(n-1):
    if len(str(a[i])) == len(str(a[i+1])):
        if len(str(a[i])) == 1:
            if a[i] == 0 and a[i+1] == 9:
                continue
            if a[i] == 0:
                a[i] = a[i+1] + 1
            elif a[i+1] == 9:
                a[i+1] = a[i]-1
            else:
                a[i] = a[i+1] + 1
            print(" ".join(map(str, a)))
            break
        else:
            sa = str(a[i])
            sai = str(a[i+1])
            if int(sa[1:]) > int(sai[1:]):
                a[i] = int(sai[0]+sa[1:])
                print(" ".join(map(str, a)))
                break
            if sa[0] == "1" and sai[0] == "9":
                continue
            if sa[0] == "1":
                a[i] = int(str(int(sai[0])+1)+sa[1:])
                print(" ".join(map(str, a)))
                break
            if sai[0] == "9":
                a[i+1] = int(str(int(sa[0])-1)+sai[1:])
                print(" ".join(map(str, a)))
                break
            a[i] = int(str(int(sai[0])+1)+sa[1:])
            print(" ".join(map(str, a)))
            break
else:
    print("impossible")