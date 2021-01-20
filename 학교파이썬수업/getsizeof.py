import sys

#전역 변수 선언 부분
intVar, floatVar, boolVar, strVar, listVar, tupleVar, dictVar, setVar = [None] * 8
#미리 메인 코드에서 사용할 변수들을 선언하는 전역 변수 선언하기
#[None]으로 해서 변수 값 없는 상태로 (전역변수) 선언하기
#거기다가 *8하는 이유는 전역 변수 8개 선언해주었으니 변수 8개 모두 값 없는 [None] 상태임을 표시
#따라서 전역변수 8개 선언하면서 변수값은 없는 상태를 변수명, 변수명 ...(8개) = [None] *8 로 해줌

#메인 코드 부분
if __name__ == '__main__':
    #위에서 선언한 전역 변수 8개의 초기값 선언하기
    intVar = 0
    floatVar =0.0
    boolVar = True
    strVar=''
    listVar =[]
    tupleVar=()
    dictVar={}
    setVar=set()

    print(sys.getsizeof(intVar), sys.getsizeof(floatVar), sys.getsizeof(boolVar), sys.getsizeof(strVar), sys.getsizeof(listVar), sys.getsizeof(tupleVar), sys.getsizeof(dictVar), sys.getsizeof(setVar))
    #sys모듈 안의 getsizeof()함수 사용하여 각 변수의 데이터 크기를 출력하기
