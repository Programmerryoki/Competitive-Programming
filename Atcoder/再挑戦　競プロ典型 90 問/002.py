def main():
    def right(bracket):
        check = 0
        for b in bracket:
            if b == "(":
                check += 1
            else:
                check -= 1
            if check < 0:
                return False
        return check == 0

    N = int(input())
    if N&1:
        exit()
    ans = []
    for n in range(2**N):
        num = bin(n)[2:]
        if num.count("1") != N//2:
            continue
        num = "0"*(N - len(num)) + num
        brac = []
        for i in num:
            if i == "0":
                brac.append("(")
            else:
                brac.append(")")
        if right(brac):
            ans.append("".join(brac))
    ans.sort()
    print("\n".join(ans))


if __name__ == '__main__':
    main()