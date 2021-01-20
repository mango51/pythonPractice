answernum = int(input('')) #숫자를 입력받는 변수
answercount = 0 #숫자를 하나씩 올려나갈 변수

#list() 함수는 문자열을 한 글자씩 잘라주는 함수
#예를 들어 a = list('apple')이라고 하면 a=['a','p','p','l','e']로 입력한 문자열이 잘려서 리스트로 출력


for i in range(1, answernum+1):
    number = str(i)
    game = list(number)
    #입력한 수까지 돌기 > number는 1~입력한 수까지 돌기
    #입력한 수를 문자열로 바꾼 후, list형식으로 나눠서 변수 game에 넣기
    
    for a in range(0, len(number)):
        # a= len('apple')이라고 하면 a= 5가 됨
        #number 글자를 list로 나눈 game을 한 번 쭉 훑기
        #len(number)는 글자 개수이며 리스트로 나뉜 game을 하나하나 확인해줄 수 있음
        if '3' in game[a]:
            answercount += 1
        elif '6' in game[a]:
            answercount += 1
        elif '9' in game[a]:
            answercount += 1
    #elif문은 if문이 실행되어도 넘어와서 실행됨
    #3,6,9 있으면 있을 때마다 count에 일씩 더해짐

    #만약 12를 입력했을 때, answernum=12이고 1~12까지 돌아가는데
    #number = 1~12까지 돌아가면서 369확인
    #number에 1~12 문자열로 저장되는데 game에서 number를 list형식으로 바꿔둠
    #game에서 해당 숫자(포문으로 돌아가는 숫자) number가 list형식으로 되어 있는데 number를 len(number)로 하여 문자열의 길이를 포문으로 돌리기
    #이렇게 포문으로 돌리면 문자 하나하나 확인 가능
    #len(number)로 만약 끝까지 와서 number =12이면 len(number) = 2이고 game=['1','2']이다.
    #len(number)로 0,1 총 2번 작은 포문에서 돌리는데 우선 game[0]에서 이프문에 맞는게 있는지 보고 그 다음에 game[1]에서 이프문에 맞는게 있는지 확인한다
    #해당 조건에 성립하는게 있으면 이프문에 해당하는 명령문 실행 (answercount에 하나씩 더하기)
    #이렇게 될 경우, 12까지의 수에서 369 성립하여 박수친 횟수 알 수 있음!

print(answercount)
