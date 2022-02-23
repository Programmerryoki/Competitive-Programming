import heapq
from collections import deque

while True:
    try:
        n = int(input())
    except:
        break

    stack = []
    so = []
    que = deque()
    qo = []
    heap = []
    ho = deque()
    output = []
    valid = True
    for _ in range(n):
        cmd, x = [int(i) for i in input().split()]
        if cmd == 1:
            stack.append(x)
            que.appendleft(x)
            heapq.heappush(heap, -x)
        else:
            try:
                output.append(x)
                so.append(stack.pop())
                qo.append(que.pop())
                ho.append(-heapq.heappop(heap))
            except:
                valid = False
        # print(output)
        # print(stack, que, heap)
        # print(so, qo, ho)
        # print()
    ho = list(ho)
    # print(output)
    # print(so, qo, ho)
    os = output == so
    oq = output == qo
    oh = output == ho
    if not valid:
        print("impossible")
        continue
    if os and oq and oh:
        print("not sure")
    elif (os and oq) or (oq and oh) or (os and oh):
        print("not sure")
    elif os:
        print("stack")
    elif oq:
        print("queue")
    elif oh:
        print("priority queue")
    else:
        print("impossible")