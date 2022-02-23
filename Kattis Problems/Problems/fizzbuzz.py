n = list(map(int, input().rstrip().split(" ")))
for a in range(1, n[2]+1):
    if a%n[0]==0 and a%n[1]==0:
        print("FizzBuzz")
    elif a%n[0]==0:
        print("Fizz")
    elif a%n[1]==0:
        print("Buzz")
    else:
        print(a)