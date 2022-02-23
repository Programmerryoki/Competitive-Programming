cards = input()
type = "TCG"
count = [0]*3
for i in cards:
    count[type.index(i)] += 1
print(min(count)*7 + sum([i**2 for i in count]))