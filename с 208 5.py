if __name__ == "__main__":
    with open("file 3.txt", "r", encoding="utf-8") as f:
        a = f.readlines()
    print(len(set(a)))
    print()

    for i in set(a):
        c = 0
        for k in a:
            if (k == i):
                c += 1
        print(i, c)
