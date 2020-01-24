myFile = open("tests.txt")
n_line = 1
n = a = b = 0

for line in myFile:
    if n_line != 1:
        s = line.rstrip('\n').split(' ')
        n = float(s[0])
        a = float(s[1])
        b = float(s[2])
        if b == 0:
            if a == 1:
                res = n
            if a < 1:
                res = 0
            if a > 1:
                res = -1
        else:
            if n <= 0:
                res = 0
            if (n > 0) and (n < a/b):
                res = (a-1)/b
                if res < 0:
                    res = 0
            if n > a/b:
                res = 0


        res = round(res,4)

       # print("{0:g}".format(res))
        print(res)
    n_line += 1