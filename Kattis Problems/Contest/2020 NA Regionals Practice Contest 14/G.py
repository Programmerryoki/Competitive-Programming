from collections import defaultdict
from sys import stdin

def main():
    input = stdin.readline
    MOD = 10**9 + 7
    n = int(input())
    songs = [int(i) for i in input().split()]
    count = 0
    ones = {}
    dic = {}
    for i in range(n):
        if songs[i] == 1:
            if count in ones:
                ones[count] += 1
            else:
                ones[count] = 1
        elif songs[i] == 2:
            count += 1
        else:
            for key in ones:
                n = count - key
                if n in dic:
                    dic[n] += ones[key]
                else:
                    dic[n] = ones[key]
    total = 0
    for key in dic:
        total += (2**key - 1) * dic[key]
    # for i,n in enumerate(dic):
    #     total += (2**i - 1) * n
    print(total%MOD)

if __name__ == "__main__":
    main()