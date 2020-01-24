n = 1.695
a = 0.420
b = 0.420
#1.695 0.420 0.420

#0.394 2.464 0.000

for i in range(10):
    ni = n*n*(-b)+a*n
    print(ni)
    n = ni
