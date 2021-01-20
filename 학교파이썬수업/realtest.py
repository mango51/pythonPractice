guguline=''
for i in range(1,10):
    guguline=''
    for k in range(2,10):
        guguline= guguline + str('%2d X %2d = %2d' %(i,k,i*k))
    print(guguline)
