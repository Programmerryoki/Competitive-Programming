w = input()
c = 0
while True:
    line = input()
    if line == "END_OF_TEXT":
        break
    line = line.lower().split()
    c += line.count(w)
print(c)