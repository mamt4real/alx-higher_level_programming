#!/usr/bin/python3

for i in range(8):
    for j in range(10):
        if j <= i:
            continue
        print(f"{i:d}{j:d}", end=', ')
print(89)
