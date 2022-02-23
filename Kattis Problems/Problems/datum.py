d, m = list(map(int, input().split()))
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
month = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
rem = 3
for a in range(m-1):
    rem = (rem + month[a])%7
rem = (rem + d)%7
print(week[rem])