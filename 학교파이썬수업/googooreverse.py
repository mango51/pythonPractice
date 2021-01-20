i =0
num =0

num = int(input('단 입력 : '))

for i in range(9,0,-1):
    print('%d X %d = %d' %(num,i,num*i))

# -1 써줘야 -1씩 감소함 >> 9,8,7,6,5,4,3,2,1 이렇게 -1로 감소
