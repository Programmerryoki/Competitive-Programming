def value(n):
    return sum(ord(s.lower()) - ord('a') + 1 for s in n)

with open('0022.txt', 'r') as file:
    names = file.readline().replace('"', '').split(",")
names.sort()
total = 0
for i in range(len(names)):
    total += (i + 1) * value(names[i])
print(total)