line = input()
diff = 0
for a in range(len(line)):
    if a%3==0 and line[a] != "P":
        diff += 1
    elif a%3==1 and line[a] != "E":
        diff += 1
    elif a%3==2 and line[a] != "R":
        diff += 1
print(diff)