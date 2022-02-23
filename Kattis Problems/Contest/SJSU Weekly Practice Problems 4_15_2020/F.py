from sys import stdin

def main():
    input = stdin.readline
    n, m = [int(i) for i in input().split()]
    c = 0
    stat = [-m-1]*n
    sche = [tuple(int(i) for i in input().split()) for j in range(n)]
    sche.sort()
    for a,s in sche:
        # a,s = vals
        fp = -1
        for i in range(len(stat)):
            if stat[i] <= a:
                if fp == -1:
                    fp = i
                if stat[i] + m >= a:
                    stat[i] = a + s
                    break
        else:
            c += 1
            # if fp == -1:
            #     stat.append(a+s)
            # else:
            stat[fp] = a+s
    print(n - c)

if __name__ == '__main__':
    main()



# n, m = [int(i) for i in input().split()]
# c = 0
# stat = []
# sche = [[int(i) for i in input().split()] for j in range(n)]
# sche.sort()
# for vals in sche:
#     a,s = vals
#     print(stat, a, s, c)
#     for i,t in enumerate(stat):
#         if t <= a:
#             if t + m < a:
#                 c += 1
#             stat[i] = a + s
#             break
#     else:
#         c += 1
#         stat.append(a+s)
# print(n - c)