while True:
    n = int(input())
    if n == 0:
        break
    s = [int(i) for i in input().split()]
    av = sum(s)/len(s)
    var = sum([(i - av)**2 for i in s])/n
    print(var**0.5)