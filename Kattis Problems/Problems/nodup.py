line = input().split()
print("yes") if len(line) == len(set(line)) else print("no")