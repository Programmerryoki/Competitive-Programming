t = int(input())
for _ in range(t):
    d,m = input().split()
    d = int(d)
    if m == "Jan":
        if d <= 20:
            print("Capricorn")
        else:
            print("Aquarius")
    if m == "Feb":
        if d <= 19:
            print("Aquarius")
        else:
            print("Pisces")
    if m == "Mar":
        if d <= 20:
            print("Pisces")
        else:
            print("Aries")
    if m == "Apr":
        if d <= 20:
            print("Aries")
        else:
            print("Taurus")
    if m == "May":
        if d <= 20:
            print("Taurus")
        else:
            print("Gemini")
    if m == "Jun":
        if d <= 21:
            print("Gemini")
        else:
            print("Cancer")
    if m == "Jul":
        if d <= 22:
            print("Cancer")
        else:
            print("Leo")
    if m == "Aug":
        if d <= 22:
            print("Leo")
        else:
            print("Virgo")
    if m == "Sep":
        if d <= 21:
            print("Virgo")
        else:
            print("Libra")
    if m == "Oct":
        if d <= 22:
            print("Libra")
        else:
            print("Scorpio")
    if m == "Nov":
        if d <= 22:
            print("Scorpio")
        else:
            print("Sagittarius")
    if m == "Dec":
        if d <= 21:
            print("Sagittarius")
        else:
            print("Capricorn")