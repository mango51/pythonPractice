#변수 선언 부분
i, k, heartNum=0,0,0
numStr, ch,heartStr='','',''

#메인 코드 부분
if __name__ == '__main__':
    numStr = input('숫자를 여러 개 입력하세요 : ')
    print('')
    i=0
    ch=numStr[i] #입력한 수 각자리수로 나눠서 추출
    while True:
        heartNum=int(ch) #하나의 자리수를 숫자로 변환
        #밑에서 반복문으로 올라온 경우, ch=numStr[i]로 i+=1한 상태로 왔기에 다음 자리수를 숫자로 변환시키기
        heartStr=''
        #밑에서 반복문이 올라올 경우를 대비하여 heartStr은 초기화시킴
        #기존에 써왔던 값이 남아있을 수 있기 때문

        for k in range(0,heartNum): #해당 숫자만큼 돌리기
            heartStr += '\u2665' #누적변수 heartStr로 하트 추가하기
            #해당 숫자만큼 하트에 추가되어 하트는 해당 숫자 갯수만큼 있음

        print(heartStr) #하트 출력 (한 행)

        i+=1 #다음 자리수로 이동

        if(i>len(numStr)-1): #numStr이 4자리 수 입력하면 len(numStr)=4
            break #i는 0~len(numStr)-1까지 있음
            #i가 len(numStr)이면 numStr가 있는 자리수에서 넘어가기 때문에 반복 멈추기
        ch = numStr[i]
        #다음 자리 수로 이동한 i (i+=1을 위에서 했기 때문에) 로 ch값 대입하기
        #ch=numStr[i]는 i+=1로 다음 자리수의 값 ch가 되어버리고 다시 반복문 시작
