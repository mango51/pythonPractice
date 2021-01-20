import sys

basket =[]
while (1):
    print()
    print('======================')
    print('코디의 장바구니입니다.')
    print('======================')
    print('1. 담겨있는 물건 확인하기')
    print('2. 물건 추가하기')
    print('3. 물건 삭제하기')
    print('0. 프로그램 종료')
    print('======================')
    number = input('무엇을 하실 건가요? (숫자 입력) : ')

    if number == '1':
        if len(basket) != 0:
            print(basket)
        else:
            print('아무 것도 없습니다.')
    elif number == '2':
        while(1):
            print("추가할 항목을 입력해주세요. 더 이상 추가할 항목이 없으면 \'그만\'을 입력해주세요.")
            adding = input()
            if adding == '그만':
                print('장바구니 담기를 종료합니다.')
                break
            else:
                basket.append(adding)
                continue
    elif number == '3':
        while(1):
            print(basket)
            print('현재 담겨있는 장바구니 목록입니다. 삭제하실 항목을 입력해주세요.')
            print('삭제 메뉴를 종료하시면 0을 입력해주세요.')
            subtracting = input()
            for i in range(0,len(basket)):
                if subtracting == basket[i]:
                    del basket[i]
                    print('삭제가 완료되었습니다.') #실행되었기에 'elif 패스'하고 밑의 if문 실행하려지만 조건 맞지 않아서 다시 while문 처음으로 돌아가기
                elif subtracting != basket[i]:
                    if i == len(basket)-1: #끝까지 돌고도 삭제할 값 없으면 마지막에 출력하기
                        if subtracting != '0':
                            print('잘못된 값을 입력하셨습니다. 다시 입력해주세요.')
            if subtracting =='0':
                break
    elif number=='0':
        sys.exit()
    else:
        print('잘못입력했습니다.다시입력해주세요.')
