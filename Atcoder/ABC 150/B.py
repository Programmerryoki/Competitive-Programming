import re

n = int(input())
s = input()
print(len(re.findall(r"ABC", s)))