def main():
    N = int(input())
    A = [int(i) for i in input().split()]

    def score(x):
        total = 0
        for a in A:
            total += x + a - min(a, 2*x)
        return total / N

    low = 0
    high = 10**10
    ls = score(low)
    hs = score(high)
    for _ in range(400):
        mid = (low + high) / 2
        ms = score(mid)
        if ls < hs:
            high = mid
            hs = ms
        else:
            low = mid
            ls = ms
    # print(low, high, ls, hs)
    print(ls)

if __name__ == '__main__':
    main()