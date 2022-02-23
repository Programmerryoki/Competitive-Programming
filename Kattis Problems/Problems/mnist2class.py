import random
for a in range(30):
    print(" ".join([str((-1) ** random.randint(0,3)) for i in range(51)]))