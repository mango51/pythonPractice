aa=[]
bb=[]

for i in range(0,200):
    aa.append(i*3)

for i in range(0,200):
    bb.append(aa[199-i])

print('bb[0] = %d, bb[199]=%d'%(bb[0],bb[199]))
