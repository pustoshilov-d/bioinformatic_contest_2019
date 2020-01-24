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
            print(res)
        else:
            n0 = n
            for i in range(100001):

                ni = n*n*(-b) + a*n
                if i == 100000:
                    if ni<0:
                        print(0)
                    else:
                        print(round(ni,4))
    """"          if (ni <= 0) and (i > 1000):
                       print(0)
                       break
                   if i== 9999 and (abs(ni-n) < 0.0001) and (n > 0):
                       print(round(n,4))
                       break
                   if i == 1000:
                       print('nope 2')
                   n = ni
                     """

    n_line += 1