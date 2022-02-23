while True:
    x,y = [int(i) for i in input().split()]
    if x == y == 0:
        break
    if x+y == 13:
        print("Never speak again.")
    elif x < y:
        print("Left beehind.")
    elif x == y:
        print("Undecided.")
    else:
        print("To the convention.")