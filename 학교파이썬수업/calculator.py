# 종합 계산기 프로그램

# 변수 선언 부분 (사용하는 변수들 초기값 선언하기)
select, answer, numStr, num1, num2 = 0,0,'',0,0

# 메인 코드 부분
select = int(input('1. 입력한 수식 계산 2. 두 수 사이의 합계 : '))

# 1. 수식계산기
if select == 1:
    numStr = input('수식을 입력하세요 : ')
    answer = eval(numStr) #eval(수식) 함수 : 수식을 계산하는 기능
    print('%s 결과는 %5.1f입니다.' %(numStr, answer))
# 2. 두 수 사이의 합계 (두 숫자 사이의 모든 수를 더한 합계)
elif select ==2:
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))
    for i in range(num1, num2+1):
        answer += i
    print('%d+...+%d는 %d입니다.' %(num1, num2, answer))
# 1,2 아닌 다른 것 입력했을 경우 
else:
    print('1 또는 2만 입력해야합니다.')
