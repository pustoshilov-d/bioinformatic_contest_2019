
myFile = open('input2.txt')
n = 0
cur_line = ""

for line in myFile:
    if n != 0:
        if n % 2 == 1:
            cur_line = line.rstrip('\n')
        else:
            s = ""
            flag = cur_line.find(line.rstrip('\n')) + 1
            while flag != 0:
                s = s + ' ' + str(flag)
                flag = cur_line.find(line.rstrip('\n'),flag) + 1
            print(s[1:])

    n += 1
