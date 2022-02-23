from sys import stdin

def countMax(nums, lst):
    md = 0
    for num in nums:
        dif = sum([num[i] == lst[i] for i in range(len(lst))])
        if md < dif:
            md = dif
    return md

def main():
    input = stdin.readline

    n,k = map(int, input().split())
    count = [[0,0] for i in range(k)]
    nums = [input() for i in range(n)]
    for i in range(n):
        num = nums[i]
        for j in range(k):
            count[j][num[j] == "1"] += 1

    best = [str(int(min(i)!=i[0])) for i in count]
    dif = countMax(nums, best)
    for _ in range(k):
        tMin = float("inf")
        tLst = []
        for i in range(k):
            tmp = [i for i in best]
            tmp[i] = str(1 - int(tmp[i]))
            t = countMax(nums, tmp)
            if t < tMin:
                tMin = t
                tLst = tmp
        if tMin < dif:
            dif = tMin
            best = tLst
    print("".join(map(str, best)))

if __name__ == "__main__":
    main()