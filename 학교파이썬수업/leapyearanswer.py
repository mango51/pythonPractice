#전역변수 선언하기
year =0

#메인코드 부분
if __name__ == '__main__': # 여기가 메인 함수 부분이다
    #if __name__ = '__main__': 코드는 여기가 메인 함수임을 표시하는 것
    year = int(input('연도를 입력하세요 : '))

    if((year%4==0) and (year%100 != 0) or (year%400==0)):
        # % 산술연산자, == 비교연산자(동등연산자), and 논리연산자
        # 산술연산자 > 비교연산자 > 논리연산자
        # 논리 연산자 중에서는 and > or
        # 따라서 가로 안에 있는 코드 연산 후 and > or에 따라
        # 우선 (year%4==0)and(year%100!=0)연산하고
        # 그 다음에 연산된 (year%4==0)and(year%100!=0)  or  (year%400==0)으로 연산하기
        # year = 400일 때, (true and false or true) 1 and 0 or 1 = 1임 (true라서 코드 실행)
        print('%d년은 윤년입니다.' %year);
    else:
        print('%d년은 윤년이 아닙니다.'%year);
