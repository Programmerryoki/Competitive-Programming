from sys import stdin

def main():
    input = stdin.readline
    string = input()
    ls = ""
    for i in range(len(string)-1):
        for j in range(i+1, len(string)):
            t = [i,j]
            while t[0] < len(string) and t[1] < len(string) and string[t[0]] == string[t[1]]:
                t[0] += 1; t[1] += 1

            if string[t[0]-1] == string[t[1]-1]:
                if t[0]-i > len(ls):
                    ls = string[i:t[0]]
                elif t[0]-i == len(ls):
                    ls = min(string[i:t[0]], ls)
            elif string[t[0]-2] == string[t[1]-2]:
                if t[0]-i-1 > len(ls):
                    ls = string[i:t[0]-1]
                elif t[0]-i-1 == len(ls):
                    ls = min(string[i:t[0]-1], ls)
    print(ls)

if __name__ == "__main__":
    main()