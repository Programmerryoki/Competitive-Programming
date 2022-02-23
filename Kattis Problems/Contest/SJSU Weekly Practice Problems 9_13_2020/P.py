from sys import stdin

def main():
    input = stdin.readline
    N,Q = [int(i) for i in input().split()]
    bit = [0]*(N+1)
    ans = []
    for _ in range(Q):
        o,*r = input().split()
        if o == "+":
            i,a = map(int, r)
            i += 1
            while i <= N:
                bit[i] += a
                i += i & -i
        else:
            i = int(r[0])
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            ans.append(s)
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()