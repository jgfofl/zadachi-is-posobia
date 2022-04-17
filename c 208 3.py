a = []
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        a.append(line)
        maximum = 0
        for i in a:
            if len(i) < maximum:
                maximum = len(i)
            elif len(i) == maximum:
                print(i)
print(i)
