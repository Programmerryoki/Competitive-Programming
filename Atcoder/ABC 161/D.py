K = int(input()) - 1
nums = [str(i) for i in range(1,10)]
while True:
    # print(nums)
    if K < len(nums):
        print(nums[K])
        break
    else:
        K -= len(nums)

    que = []
    for n in nums:
        if n[-1] > "0":
            que.append(n + str(int(n[-1]) - 1))
        if n[-1] < "9":
            que.append(n + str(int(n[-1]) + 1))
        que.append(n + n[-1])
    que.sort()
    nums = que