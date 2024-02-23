count = sum(1 for line in open('filename.txt') for c in line if c.isupper())
print(count)
