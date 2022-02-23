nums = ["ham", "hamu"]
num = ""
n = input()
i = 0
while i < len(n):
    if n[:4] == nums[1]:
        num += "1"
        n = n[4:]
    elif n[:3] == nums[0]:
        num += "0"
        n = n[3:]
print("".join(map(lambda x: nums[int(x)], list(num+"0") if num != "0" else list(num))))