import re
from sys import stdin

for line in stdin.readlines():
    if re.search("problem", line.lower()):
        print("yes")
    else:
        print("no")