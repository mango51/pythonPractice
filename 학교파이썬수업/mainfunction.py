#함수 선언 부분
def myFunc():
    print('함수 호출')

#전역 변수 선언 부분
gVar=100

#메인 코드 부분
if __name__ == '__main__': #여기는 메인 코드 부분입니다 암시하는 코드
    print('메인 함수 부분이 실행됩니다.')
    myFunc()
    print('전역 변수 : ', gVar)
