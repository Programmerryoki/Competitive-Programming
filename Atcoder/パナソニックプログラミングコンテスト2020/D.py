ans = []
type = [[1]]
que = []
N = int(input())
for i in range(N-1):
    que = type
    type = []
    while len(que) != 0:
        t = que.pop()
        ma = max(t)
        for j in range(1,ma+2):
            type.append(t + [j])
type.sort()
char = " abcdefghijklmnopqrstuvwxyz"
for a in type:
    print("".join(map(lambda x: char[x], a)))


# ans = []
# type = [[1]]
# que = []
# N = int(input())
# for i in range(N-1):
#     que = type
#     type = []
#     while len(que) != 0:
#         t = que.pop()
#         ma = max(t)
#         type.append(t + [ma])
#         type.append(t + [ma+1])
# type.sort()
# char = " abcdefghijklmnopqrstuvwxyz"
# for a in type:
#     print("".join(map(lambda x: char[x], a)))