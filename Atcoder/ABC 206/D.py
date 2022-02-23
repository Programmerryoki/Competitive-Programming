from sys import stdin

def main():
    input = stdin.readline

    N = int(input())
    A = [int(i) for i in input().split()]
    SA = set(A)
    con = {i:i for i in SA}
    rev = {i:{i} for i in SA}
    total = 0
    for i in range(N // 2):
        n1 = con[A[i]]
        n2 = con[A[N-i-1]]
        if n1 == n2:
            continue

        total += 1
        sm = lm = None
        s = l = None
        if len(rev[n1]) < len(rev[n2]):
            sm, lm = rev[n1], rev[n2]
            s, l = n1, n2
        else:
            sm, lm = rev[n2], rev[n1]
            s, l = n2, n1

        for n in sm:
            con[n] = l
            if n not in lm:
                lm.add(n)
        sm.clear()
    print(total)

if __name__ == '__main__':
    main()