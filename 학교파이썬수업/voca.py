voca={}
tempList=[]
temp=""
menu=0

while (True):
    menu = input("메뉴를 선택하세요. (단어 입력=1, 단어 출력=2, 단어 검색=3, 종료 =0) ")

    if menu=='1':
        temp = input("등록할 단어 입력(영어-한글) : ")
        temp = temp.split('-')
        for i in range(0,len(temp)):
            tempList.append(temp[i])
        voca[tempList[0]]=tempList[1]
        tempList=[]
    elif menu=='2':
        print(" [단어장 출력]")
        a = list(voca.keys())
        b=list(voca.values())
        for i in range(0,len(a)):
            print(a[i],'(',b[i],')')
    elif menu=='3':
        temp = input("검색할 단어 : ")
        print('[검색 결과]')
        if temp in voca:
            print(' ',temp,'(',voca[temp],')')
        else:
            print(' 등록되지 않은 단어입니다')
    elif menu=='0':
        break;
