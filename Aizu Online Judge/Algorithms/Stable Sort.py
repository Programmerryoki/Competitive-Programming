import sys


def BubbleSort(C):
    for i in range(len(C)):
        for j in range(len(C)-1, i, -1):
            if C[j][1] < C[j-1][1]:
                C[j], C[j-1] = C[j-1], C[j]


def SelectionSort(C):
    for i in range(len(C)):
        mini = i
        for j in range(i, len(C)):
            if C[j][1] < C[mini][1]:
                mini = j
        C[i], C[mini] = C[mini], C[i]


def stable(cards, C):
    for a in range(len(C)-1):
        c1 = cards.index(C[a])
        c2 = cards.index(C[a+1])
        if C[a][1] == C[a+1][1] and c1 > c2:
            print("Not stable")
            break
    else:
        print("Stable")


def main():
    input = sys.stdin.readline
    N = int(input())
    cards = input().split()
    bs = [i for i in cards]
    ss = [i for i in cards]
    BubbleSort(bs)
    SelectionSort(ss)
    print(" ".join(bs))
    stable(cards, bs)
    print(" ".join(ss))
    stable(cards, ss)


if __name__ == "__main__":
    main()