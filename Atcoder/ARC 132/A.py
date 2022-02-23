from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    R = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    ans = ""
    q = int(input())
    for _ in range(q):
        r,c = [int(i)-1 for i in input().split()]
        if R[r] + C[c] >= n + 1:
            ans += "#"
        else:
            ans += "."
    print(ans)

if __name__ == '__main__':
    main()