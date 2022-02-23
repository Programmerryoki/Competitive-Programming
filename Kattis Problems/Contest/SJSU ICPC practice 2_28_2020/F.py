from sys import stdin
import re

def main():
    ans = []
    while True:
        try:
            p = input()
            line = input()
            m = []
            for i in range(len(line)):
                if re.match(p, line[i:]):
                    m.append(i)
            # m = [m.span()[0] for m in re.finditer(p, line)]
            ans.append(m)
        except:
            break
    print("\n".join([" ".join(map(str, i)) for i in ans]))

if __name__ == "__main__":
    main()