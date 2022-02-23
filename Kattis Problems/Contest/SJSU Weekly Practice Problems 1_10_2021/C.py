numbers = [["***", "* *", "* *", "* *", "***"],
           ["  *", "  *", "  *", "  *", "  *"],
           ["***", "  *", "***", "*  ", "***"],
           ["***", "  *", "***", "  *", "***"],
           ["* *", "* *", "***", "  *", "  *"],
           ["***", "*  ", "***", "  *", "***"],
           ["***", "*  ", "***", "* *", "***"],
           ["***", "  *", "  *", "  *", "  *"],
           ["***", "* *", "***", "* *", "***"],
           ["***", "* *", "***", "  *", "***"]]

inputs = [input() for i in range(5)]
for i in range(5):
    lst = []
    string = inputs[i]
    while string:
        lst.append(string[:3])
        string = string[4:]
    inputs[i] = lst

num = ""
for i in range(len(inputs[0])):
    try:
        num += str(numbers.index([j[i] for j in inputs]))
    except:
        print("BOOM!!")
        exit()
print("BEER!!" if not int(num)%6 else "BOOM!!")