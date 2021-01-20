i, k =0,0

for i in range(2,10,1): #2~9단 반복
    for k in range(1,10,1): #각 단의 뒷자리 1~9 반복
        print('%d X %d = %d' %(i,k,i*k))
    print('')
