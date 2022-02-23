X,Y,N = [int(i) for i in input().split()]
for n in range(1,N+1):
    if n%X == 0 and n%Y == 0:
        print("FizzBuzz")
    elif n%X == 0:
        print("Fizz")
    elif n%Y == 0:
        print("Buzz")
    else:
        print(n)