n, m = [int(i) for i in input().split()]
num = m - n
if num > 1:
    print("Dr. Chaz will have %d pieces of chicken left over!"%(num))
elif num < -1:
    print("Dr. Chaz needs %d more pieces of chicken!"%(-num))
elif num == 1:
    print("Dr. Chaz will have 1 piece of chicken left over!")
else:
    print("Dr. Chaz needs 1 more piece of chicken!")