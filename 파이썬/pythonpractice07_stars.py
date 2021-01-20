lines = int(input('줄 수를 입력해주세요 : '))

number = 1
for i in range(0,lines):    
    for j in range(0,number):
        print('*',end='')
    number += 1
    print('\n')
