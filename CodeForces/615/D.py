import sys

def main():
    input = sys.stdin.readline

    q,x = [int(i) for i in input().split()]
    A = [0 for i in range(x)]
    m = 0
    c = 0
    ans = []
    for a in range(q):
        n = int(input())
        A[n%x] += 1
        while A[c] >= (m//x+1):
            c = (c+1)%x
            m += 1
        ans.append(str(m))

    print("\n".join(ans))


if __name__ == "__main__":
    main()