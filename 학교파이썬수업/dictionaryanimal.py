animals = {'개':'강아지','호랑이':'개호주','곰':'능소니','말':'조랑말','닭':'병아리','고등어':'아기생선','명태':'노가리'}

while (True):
    oneanimal = input(str(list(animals.keys())) + ' 중 새끼 이름 알고 싶은 동물은? ')

    if oneanimal in animals:
        print('<%s>의 새끼는 <%s>입니다.'%(oneanimal, animals[oneanimal]))
        # oneanimal = 키값, animals[oneanimal]= value값
        # animals[키값] = 해당 value값
    elif oneanimal=='끝':
        break
    else:
        print('보기에 없습니다')
