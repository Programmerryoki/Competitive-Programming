from sys import stdin
input = stdin.readline

def main():
    N = int(input())
    ans = [0]*(N)
    rank = 1
    score = int(input())
    for i in range(N-1):
        ans[i] = rank
        if int(input()) > score:
            rank += 1
    ans[-1] = rank
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()