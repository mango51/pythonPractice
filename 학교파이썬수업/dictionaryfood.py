#딕셔너리를 활용한 음식 궁합 출력 프로그램

foods = {'떡볶이' : '오뎅','짜장면':'단무지','라면':'김치','피자':'피클','맥주':'땅콩','치킨':'치킨무','삼겹살':'상추'}

while (True):
    myfood = input(str(list(foods.keys()))+' 중 좋아하는 음식은? ')
    #food.keys()로 key값들을 추출하여 list구조로 만들고 string 구조로 만들어 input 내용으로 두기
    if myfood in foods :
        #입력한 음식 딕셔너리에 존재할 경우 출력
        print('<%s> 궁합 음식은 <%s>입니다.'%(myfood,foods.get(myfood)))
        #myfood = 키값, foods.get(myfood)=value값
    elif myfood=='끝':
        break #끝 입력하면 무한 반복 종료
    else: #입력한 음식이 딕셔너리에 없을 경우
        print('그런 음식 없습니다. 확인해보세요')
        
