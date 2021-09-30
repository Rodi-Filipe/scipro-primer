
F=[i for i in range(0,101)]

C=[(i-32)*(5/9) for i in F]

Capprox=[(i-30)/2 for i in F]

counter=0
print('   F    C    C_approx')

while counter<=100:
    print('%5d %5.1f %7.1f' %(F[counter], C[counter],\
    Capprox[counter]))
    counter+=1
                                        


    