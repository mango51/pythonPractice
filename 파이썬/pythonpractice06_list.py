numbers = input('숫자 여러 개를 입력해주세요 : ')
numbersinlist = numbers.split()

newlist=[]
for i in range(0,len(numbersinlist)):
    newnum=int(numbersinlist[i])
    newlist.append(newnum)

print(newlist)

print('가장 큰 값 :', max(newlist))
print('가장 작은 값 :', min(newlist))
print('나머지 값의 평균 : ',sum(newlist)/len(newlist))
