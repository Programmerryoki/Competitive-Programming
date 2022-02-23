nums = input()
op = [""]*3
for i in range(2**3):
    b = bin(i)[2:]
    b = "0"*(3 - len(b)) + b
    for j in range(len(b)):
        if b[j] == "1":
            op[j] = "+"
        else:
            op[j] = "-"
    string = "".join(nums[i]+op[i] for i in range(3))+nums[-1]
    if eval(string) == 7:
        print(string + "=7")
        break