month = 3
year = 2018
y = int(input())
while year < y:
    month += 26
    year += month // 12
    month %= 12
print("yes" if year == y else "no")