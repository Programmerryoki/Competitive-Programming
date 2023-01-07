from sys import stdin

def main():
    input = stdin.readline
    N = int(input())
    T = input()
    for i in range(N):
        j = i+N-1
        for k in range(N):
            if k < i:
                if T[k] != T[j-k]:
                    break
            elif T[N+k] != T[j-k]:
                break
        else:
            print(f"{T[i:i+N][::-1]}\n{i}")
            break
    else:
        print(-1)


if __name__ == "__main__":
    main()