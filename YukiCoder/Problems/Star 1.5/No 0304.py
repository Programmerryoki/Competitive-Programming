for i in range(1000):
    print("0"*(3 - len(str(i))) + str(i), flush=True)
    if input() == "unlocked":
        break