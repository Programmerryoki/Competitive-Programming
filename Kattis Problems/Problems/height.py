n = int(input())

for a in range(n):
    nums = [int(i) for i in input().split()][1:]
    sortnum = sorted(nums)
    c = 0
    i = 0
    j = 0
    while nums != sortnum:
        #print(nums)
        while i < 20 and j < 20 and nums[i] >= nums[j]:
            j += 1
        #print(i,j, c)
        #if j < len(nums):
        num = nums.pop(i)
        nums.insert(j-1, num)
        i += 1
        c += j - i
        if i == 20:
            i = 0
        j = i
    #print(nums)
    print(a+1, c)