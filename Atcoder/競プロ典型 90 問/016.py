def main():
    N = int(input())
    A,B,C = [int(i) for i in input().split()]
    count = float("inf")
    for i in range(9999):
        for j in range(9999 - i + 1):
            s = A*i + B*j
            if (N-s) >= 0 and (N - s) % C == 0:
                d = i+j+((N-s)//C)
                if d < count:
                    count = d
    print(count)

if __name__ == '__main__':
    main()