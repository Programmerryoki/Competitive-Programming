N = input()
nums = [0]*10
for n in N:
    nums[int(n)] += 1
print("".join([str(i)*nums[i] for i in range(9, -1, -1)]))