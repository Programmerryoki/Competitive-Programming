from sys import stdin

def main():
    input = stdin.readline

    q = int(input())
    for _ in range(q):
        n,m = [int(i) for i in input().split()]
        cus = []
        for _ in range(n):
            cus.append([int(i) for i in input().split()])

        t = 0
        lp = m
        hp = m
        for i in range(len(cus)):
            c = cus[i]
            print(c)
            ct = c[0] - t
            lp = min(lp - ct, hp - ct)
            hp = max(hp + ct, lp + ct)
            print(t, m, lp, hp)
            if (lp < c[1] and hp < c[1]) or (lp > c[2] and hp > c[2]):
                break
            elif lp < c[1] <= hp <= c[2]:
                lp = c[1]
            elif c[1] <= lp <= c[2] <= hp:
                hp = c[2]
            else:
                lp = min(max(c[1], lp - ct), c[2])
                hp = max(min(c[2], hp + ct), c[1])
            print(t, m, lp, hp)
            t = c[0]
        else:
            print("YES")
            continue
        print("NO")

if __name__ == "__main__":
    main()