num = 0
num2=0
result=0
i=0
#전역변수 초기값 설정

num = int(input('시프트할 숫자는? '))
num2 = int(input('출력할 횟수는? '))

for i in range(1,num2+1):
    result=num<<i
    print('%d << %d = %d' %(num, i, result))

for i in range(1,num2+1):
    result = num>>i
    print('%d >> %d = %d' %(num, i, result))
