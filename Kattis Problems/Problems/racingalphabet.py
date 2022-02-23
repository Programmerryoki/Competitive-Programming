import math
circle = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"

N = int(input())
for a in range(N):
    task = input()
    move = 0
    for b in range(len(task)-1):
        move += min(abs(circle.index(task[b]) - circle.index(task[b+1])), len(circle) - abs(circle.index(task[b]) - circle.index(task[b+1])))
    print(60.0 * math.pi / len(circle) * move / 15 + len(task))