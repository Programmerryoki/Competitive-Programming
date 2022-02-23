# n, m = [int(i) for i in input().split()]
# a = [int(i) for i in input().split()]
# if n > m:
#     print(0)
# else:
#     t = 1
#     for i in range(len(a)-1):
#         for j in range(i+1, len(a)):
#             t *= abs(a[i] - a[j])
#     print(t%m)

def main():
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    if n > m:
        print(0)
    else:
        t = [0]*m
        for i in range(len(a)-1):
            for j in range(i+1, len(a)):
                n = abs(a[i]-a[j])%m
                if n == 0:
                    break
                t[n] += 1
            else:
                continue
            break
        if t[0] != 0:
            print(0)
        else:
            ans = 1
            for i in range(1,len(t)):
                ans *= (i**(t[i]))%m
            print(ans%m)

if __name__ == "__main__":
    main()