from sys import stdin

def main():
    input = stdin.readline

    for _ in range(1000):
        sik, sjk, tik, tjk = map(int, input().split())
        difi = tik - sik
        difj = tjk - sjk

        ans = ""
        ans += ("UD"[difi > 0])*abs(difi)
        ans += ("LR"[difj > 0])*abs(difj)
        print(ans, flush=True)
        input()


if __name__ == '__main__':
    main()