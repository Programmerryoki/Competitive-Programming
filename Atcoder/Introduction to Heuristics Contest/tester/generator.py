#!/usr/bin/env python3

import sys
import random

#file = open("test.txt", "w+")
if len(sys.argv) != 2:
	file.write("Usage: {} <seed>".format(sys.argv[0]))
	exit(1)

random.seed(int(sys.argv[1]))

D = 365
c = [random.randrange(0, 101) for _ in range(26)]
s = [[random.randrange(0, 20001) for _ in range(26)] for _ in range(D)]


#file.write(str(D) + "\n")
#file.write(" ".join(map(str, c)) + "\n")
#for sd in s:
#        file.write(" ".join(map(str, sd))) + "\n")
#file.close()

print(D)
print(" ".join(map(str, c)))
for sd in s:
        print(" ".join(map(str, sd)))
