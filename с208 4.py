if __name__ == "__main__":
    with open("file.txt", "r", encoding="utf-8") as f:
        a = f.readlines()
    maximum = 0
    for i in a:
      if len(i) > maximum:
          maximum = len(i)
    for i in range(1, maximum + 1):
      for k in a:
          if len(k) == i:
              print(k)