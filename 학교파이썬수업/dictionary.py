singer = {} #빈 딕셔너리 선언

singer['이름']='트와이스' #key값은 이름, value값은 트와이스
singer['구성원 수'] = 9
singer['데뷔'] = '서바이벌 식스틴'
singer['대표곡']='SIGNAL'

for k in singer.keys():
    #딕셔너리 singer에 있는 모든 키값들 (singer.keys()) for문을 통해 하나씩 돌려넣음
    print('%s -> %s' %(k,singer[k]))
    # k는 singer.keys 중 하나인 key값, singer[k]는 singer[키값]으로 해당 value값
    # k는 키값, singer[k] = singer[키값] =해당 value값
