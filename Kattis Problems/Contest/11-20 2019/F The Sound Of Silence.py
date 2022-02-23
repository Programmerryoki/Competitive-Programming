from collections import deque

n, m, c = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]

output = []
hold = deque()
hold.extend(nums[0:m-1])
for i, num in enumerate(nums[m-1:], m-1):
    hold.append(num)
    ma = max(hold)
    mi = min(hold)
    #print(hold)
    #print(ma,mi)
    if ma - mi <= c:
        #print(hold)
        output.append(i)
    hold.popleft()

for a in output:
    print(a)