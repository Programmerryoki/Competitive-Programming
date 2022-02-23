a,b = [int(i) for i in input().split()]
if a <= 0 <= b:
    print("Zero")
elif 0 < a:
    print("Positive")
else:
    if (b - a + 1)%2 == 0:
        print("Positive")
    else:
        print("Negative")