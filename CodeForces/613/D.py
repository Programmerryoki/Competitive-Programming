def maxBit(lst,n):
    m = -1
    for a in lst:
        num = a^n
        if num > m:
            m = num
    return m

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    # print(" ".join(map(bin, a)))
    m = max(a)
    temp = maxBit(a, m)
    # print(temp, maxBit(a, -1))
    while True:
        # print(m, temp)
        m -= 1
        t = maxBit(a, m)
        if temp < t or m == 0:
            break
        else:
            temp = t
    # print(m, t)
    print(temp)

if __name__ == "__main__":
    main()