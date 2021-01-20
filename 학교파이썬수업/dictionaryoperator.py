#키로 정렬한 후 딕셔너리 추출

import operator
#operator.itemgetter()함수를 사용하려고 모듈 operator 임포트

trainDic, trainList={},[]
#빈 딕셔너리와 리스트 준비

#딕셔너리 작성
trainDic ={'Thomas':'토마스','Edward':'에드워드','Henry':'헨리','Gothen':'고든','James':'제임스'}
trainList=sorted(trainDic.items(), key=operator.itemgetter(0))
#trainDic.items() >> 키값과 value값들을 튜플 구조로 반환
#trainDic.items()를 key를 기준으로 딕셔너리 정렬
#sorted() 함수와 operator.itemgetter(0)를 통해 key 기준으로 딕셔너리 정렬
#해당 정렬된 내용을 리스트 trainList에 대입하기

print(trainList)
