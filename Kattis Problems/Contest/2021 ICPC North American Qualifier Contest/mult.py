n = int(input())
fn = float("inf")
for i in range(n):
    num = int(input())
    if fn == float("inf"):
        fn = num
    elif num % fn == 0:
        fn = float("inf")
        print(num)