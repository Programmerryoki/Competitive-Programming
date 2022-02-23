nums = set()
inputs = [i for i in input().split("+")]
for i in range(2**(len(inputs)-1)):
    string = bin(i)[2:]
    string = "0"*(len(inputs)-len(string)-1) + string
    ad = [inputs[0]]
    for j in range(len(string)):
        if string[j] == "0":
            ad.append(inputs[j+1])
        else:
            ad[-1] += inputs[j+1]
    nums.add(sum([int(i) for i in ad]))
print(len(nums))