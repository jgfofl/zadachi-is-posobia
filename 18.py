# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-
if __name__ == "__main__":
    with open("file4.txt", "r", encoding="utf-8") as f:
        a = f.readlines()
        for i in a:
            j = None
            for k in i:
                if j == i:
                    print(i)
                j = i