myFile = open("3.txt")
s=""
n = 0
for line in  myFile:
    if n == 0:
        s = line.split(' ')
        times = int(s[0])
        lens = int(s[1])
        error = int(s[2])
def lim():


speaker =""

if speaker != "Mary":
    lim(saleChacne)

    if n == 1:
        s = line.rstrip('\n')
    n += 1

my_Dict = {}

for char in range(0,len(s)-lens):
    for i in range(lens-1):
        sub = s[char:i]
        if sub not in my_Dict.keys():
            my_Dict[sub] = s.count(sub)

for sub in my_Dict:
    if my_Dict[sub] == times:
        print(sub, times)
sorted(my_Dict)
print(my_Dict)

index = ''
sub = 'TGGGACACATGCGCTGGGAGCCT'
num = 0

flag = s.find(sub) + 1
while flag != 0:
    index = index + ' ' + str(flag)
    flag = s.find(sub, flag + len(sub)) +1
print(index[1:])

