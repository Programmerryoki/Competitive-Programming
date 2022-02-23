from sys import stdin

def main():
    input = stdin.readline
    n,m = [int(i) for i in input().split()]
    words = [(input(), i) for i in range(n)]
    words.sort(key=lambda x: tuple(-ord(x[0][i]) if i&1 else ord(x[0][i]) for i in range(len(x[0]))))
    print(" ".join(map(str, [i[1]+1 for i in words])))


if __name__ == '__main__':
    main()