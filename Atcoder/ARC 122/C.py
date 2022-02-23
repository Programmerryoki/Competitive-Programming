from bisect import bisect_left

def calc(N):
    fib = [0]*131
    fib[0] = 0
    fib[1] = 1
    for i in range(2,131):
        fib[i] = fib[i-1] + fib[i-2]
    index = bisect_left(fib, N)
    print(index)
    if fib[index] != N:
        index -= 1
    for i in range(index, 0, -1):
        x = N
        y = fib[i]
        steps = 130 - i
        for j in range(steps):
            print(x,y)
            if x > y:
                x -= y
            else:
                y -= x
            if (x == 0 or y == 0):
                break
        s = x+y+j
        if s <= 130:
            step = []
            x = N
            y = fib[i]
            while x != 0 and y != 0:
                if x > y:
                    x -= y
                    step.append(3)
                else:
                    y -= x
                    step.append(4)
            if x != 0:
                for i in range(x):
                    step.append(1)
            else:
                for i in range(y):
                    step.append(2)
            return step[::-1]

N = int(input())
step = calc(N)
print(len(step))
print("\n".join(map(str, step)))

# from bisect import bisect_left
#
# def calc(N):
#     fib = [0]*131
#     fib[0] = 0
#     fib[1] = 1
#     for i in range(2,131):
#         fib[i] = fib[i-1] + fib[i-2]
#     index = bisect_left(fib, N)
#     if fib[index] != N:
#         index -= 1
#     md = float("inf")
#     for i in range(index, 0, -1):
#         x = N
#         y = fib[i]
#         steps = 130 - i
#         for j in range(steps):
#             # print(x,y)
#             if x > y:
#                 x -= y
#             else:
#                 y -= x
#             if (x == 0 or y == 0):
#                 break
#         # print(x+y+i)
#         # print(x,y)
#         md = min(md, x+y+j)
#     return md
#
# for i in range(1,10**5+1):
#     if i%1000 == 0:
#         print(i)
#     n = calc(i)
#     if n > 130:
#         break
# else:
#     print("Complete")