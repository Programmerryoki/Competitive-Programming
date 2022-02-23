import re

num = input()
num = re.sub(r"VI(?!I+)", "IV", num)
num = re.sub(r"LX(?!X+)", "XL", num)
num = re.sub(r"(?<!XX)XI(?![IV]+)", "IX", num)
num = re.sub(r"LX(?!X+)", "XL", num)
print(num)