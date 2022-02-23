from sys import stdin
input = stdin.readline

# def main():
#     while True:
#         n = int(input())
#         if n == 0:
#             break
#         for a in range(32,0,-1):
#             if (n**(1/a)).is_integer():
#                 print(a)
#                 break
#         else:
#             print(0)

def main():
    for line in stdin:
        n = int(line)
        if n == 0:
            break
        if n > 0:
            for a in range(32,0,-1):
                t = (n**(1/a))
                if t.is_integer():
                    print(a)
                    break
            else:
                print(1)
        else:
            nu = abs(n)
            temp = 0
            for a in range(32,0,-1):
                t = (nu**(1/a))
                if t.is_integer() and a%2 == 1:
                    print(a)
                    break
            else:
                print(1)

if __name__ == "__main__":
    main()