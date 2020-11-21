
lines = open("test3.txt").readlines()
with open("ans", "w") as out:
    for i in reversed(lines):
        out.write(i)

