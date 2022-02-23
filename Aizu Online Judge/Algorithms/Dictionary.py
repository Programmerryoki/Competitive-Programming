import sys
def main():
    input = sys.stdin.readline

    dic = set()
    n = int(input())
    ans = []
    for a in range(n):
        s = input()
        if "\n" in s:
            s = s[:-1]
        if s[0] == "i":
            dic.add(s[7:])
        else:
            ans.append("yes" if s[5:] in dic else "no")
    print("\n".join(ans))

if __name__ == "__main__":
    main()