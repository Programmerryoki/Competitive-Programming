from sys import stdin
from collections import Counter

def main():
    input = stdin.readline
    n = int(input())
    ws = [int(input()) for i in range(2**n)]
    wsc = Counter(ws)
    ws.sort()
    weight = []
    rem = set()
    for w in ws[1:]:
        # print(rem,w)
        if w not in rem:
            new = set()
            for i in rem | set(weight):
                new.add(i + w)
            rem |= new
            weight.append(w)
            if len(weight) == n:
                break
    # print(weight)
    for i in range(2**n):
        num = bin(i)[2:]; num = "0"*(n-len(num))+num
        s = sum([weight[i] for i in range(len(weight)) if num[i]=="1"])
        try:
            wsc[s] -= 1
        except:
            print("impossible")
            return
    for key in wsc:
        if wsc[key] != 0:
            print("impossible")
            return
    print(*weight,sep="\n")


if __name__ == "__main__":
    main()