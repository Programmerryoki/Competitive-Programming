from sys import stdin

def main():
    input = stdin.readline
    X = input().strip()
    sd = sum(int(i) for i in X)
    ans = [0]*(len(X)+2)
    for i in range(len(ans)-1):
        ss = str(sd)
        for j in range(len(ss)-1,-1,-1):
            ans[i+(len(ss)-j-1)] += int(ss[j])
        ans[i+1] += ans[i]//10
        ans[i] %= 10
        if i < len(X):
            sd -= int(X[len(X)-i-1])
    print(int("".join(str(i) for i in ans[::-1])))


if __name__ == '__main__':
    main()