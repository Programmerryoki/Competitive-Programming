def main():
    n, m = [int(i) for i in input().split()]
    wa = [0]*n
    ac = [0]*n

    for _ in range(m):
        p, s = input().split()
        if s == "WA":
            if ac[int(p)-1] == 0:
                wa[int(p)-1] += 1
        else:
            ac[int(p)-1] += 1

    print(n-ac.count(0), sum([wa[i] for i in range(n) if ac[i] >= 1]))


if __name__ == "__main__":
    main()