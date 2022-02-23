from random import randint

with open("seeds.txt", "w") as file:
    for i in range(100):
        file.write(str(randint(0,2**64-1))+"\n")