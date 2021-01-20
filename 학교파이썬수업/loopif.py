ch =''
a,b = 0,0

while True:
    a = int(input('첫번째 수: '))
    b= int(input('두번째 수 : '))
    ch = input('계산할 연산자 : ')

    if (ch == '+'):
        print('%d %c %d = %d' %(a,ch,b,a+b))
    elif (ch=='-'):
        print('%d %c %d = %d' %(a,ch,b,a-b))
    elif (ch=='*'):
        print('%d %c %d = %d' %(a,ch,b,a*b))
    elif (ch=='/'):
        print('%d %c %d = %d' %(a,ch,b,a/b))
    elif (ch=='%'): # 나머지를 구하기
        print('%d %c %d = %d' %(a,ch,b,a%b))
    elif (ch=='//'): # 몫을 구하기
        print('%d %s %d = %d' %(a,ch,b,a//b))
    elif(ch=='**'): # 제곱하기
        print('%d %s %d = %d' %(a,ch,b,a**b))
        # %s = 문자열 (문자가 두개 이상일 때 사용)
    else:
        print('연산자를 잘못 입력하였습니다.')
    print('')
