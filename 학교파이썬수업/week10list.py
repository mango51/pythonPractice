list1=[]
list2=[]
value=0

for i in range(0,4):
    for k in range(0,5):
        list1.append(value)
        value +=3
    list2.append(list1) #2차원 배열된 list2 (1차원 배열 list1 append함으로써)
    list1=[] #list1 다시 초기화해서 다시 시작하기 (새로운 값들 리스트에 넣기)

for i in range(0,4):
    for k in range(0,5):
        print('%3d'%list2[i][k],end='')
    print('') #1행 끝날 때마다 다음 줄로 넘어가기
