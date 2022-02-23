import math
numElem = int(input())


def binSearch(x, arr):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == x:
            return m
        elif arr[m] < x:
            l = m+1
        elif arr[m] > x:
            r = m-1
    return -1


nums = []
total = 0
# As elements come in, you use binary search to see where it would go
for i in range(numElem):
    element = int(input())
    nums.append(element)
    # index = binSearch(element, nums)
    # nums.insert(index, element)
    # print("index", index, nums)

# Sort then for each element do binary search for its position
sortedNums = sorted(nums)
print(nums)
print(sortedNums)
tot = 0
for i, elem in enumerate(nums):
    position = binSearch(elem, sortedNums)
    print("pos", elem, position, i)
    tot += max(position - i, 0)
print(tot)