myFile = open("tests.txt")
n_line = 1
n = a = b = 0

for line in myFile:
    if n_line != 1:
        s = line.rstrip('\n').split(' ')
        L = s[0]
        n = s[1]
        p = float(s[2])
        k = s[3]

    n_line += 1