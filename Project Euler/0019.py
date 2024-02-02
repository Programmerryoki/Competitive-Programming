from datetime import date, timedelta

td = 0
start = date(1901, 1, 1)
end = date(2000, 12, 31)
for d in range((end - start).days + 1):
    t = start + timedelta(days=d)
    if t.day == 1 and t.isoweekday() == 7:
        td += 1
print(td)