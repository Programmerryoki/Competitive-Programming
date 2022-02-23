line = input()
print("yes" if len(line.split()) == len(set(line.split())) else "no")