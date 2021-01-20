print('연산 1')
print('x','y','cin','s','cout')
x=0
y=0
cin=0
s = (x^y)^cin #s를 구하는 식
cout = cin & (x^y) | (x&y) #cout를 구하는 식
print('%d  %d  %d  %d  %d' %(x,y,cin,s,cout))

cin=1
s = (x^y)^cin
cout = cin & (x^y) | (x&y)
print('%d  %d  %d  %d  %d' %(x,y,cin,s,cout))

y=1
cin=0
s = (x^y)^cin
cout = cin & (x^y) | (x&y)
print('%d  %d  %d  %d  %d' %(x,y,cin,s,cout))

cin=1
s = (x^y)^cin
cout = cin & (x^y) | (x&y)
print('%d  %d  %d  %d  %d' %(x,y,cin,s,cout))

x = 1
y=0
if cout ==1: 
    cin=0
s = (x^y)^cin
cout = cin & (x^y) | (x&y)
print('%d  %d  %d  %d  %d' %(x,y,cin,s,cout))

cin=1
s = (x^y)^cin
cout = cin & (x^y) | (x&y)
print('%d  %d  %d  %d  %d' %(x,y,cin,s,cout))

y=1
if cout==1:
    cin=0
s = (x^y)^cin
cout = cin & (x^y) | (x&y)
print('%d  %d  %d  %d  %d' %(x,y,cin,s,cout))

if cout==1: # full adder 연산으로 이번 cout값이 1일 경우, 다음 full adder에서는 cin 값이 1
    cin=1
s = (x^y)^cin
cout = cin & (x^y) | (x&y)
print('%d  %d  %d  %d  %d' %(x,y,cin,s,cout))

print()
print('연산 2')
a = int(input('덧셈할 두 개의 수 중 하나를 입력해주세요 : '))
b = int(input('덧셈할 나머지 수를 입력해주세요 : '))

if a>16 or b >16:
    print('오버플로우')
else:
    print('x','y','cin','s','cout')
    bina = int(format(a, 'b')) # 입력한 값 2진수로 변환시키기
    binb = int(format(b, 'b'))
    binab = int(format(a+b,'b')) #입력한 값들의 합 2진수로 변환시키기

    dividing1=[] 
    divide1= bina//1000
    divide2 = (bina-(divide1*1000))//100
    divide3 = (bina-(divide1*1000+divide2*100))//10
    divide4 = bina%10
    dividing1.append(divide1)
    dividing1.append(divide2)
    dividing1.append(divide3)
    dividing1.append(divide4) # 각 자리의 수를 하나의 원소로 하여 리스트에 추가하기

    dividing2=[]
    divide5= binb//1000
    divide6 = (binb-(divide5*1000))//100
    divide7 = (binb-(divide5*1000+divide6*100))//10
    divide8 = binb%10
    dividing2.append(divide5)
    dividing2.append(divide6)
    dividing2.append(divide7)
    dividing2.append(divide8)

    dividing3=[]
    divide9= binab//1000
    divide10 = (binab-(divide9*1000))//100
    divide11 = (binab-(divide9*1000+divide10*100))//10
    divide12 = binab%10
    dividing3.append(divide9)
    dividing3.append(divide10)
    dividing3.append(divide11)
    dividing3.append(divide12)

    cout=0
    cin=0
    for i in range(3,-1,-1): #역순으로 진행하기
        if (dividing1[i]==1) and (dividing2[i]==1): #다음 full adder에서 올릴 값인 cout값 1로 정하기
            cout=1
        else:
            cout=0
        print(dividing1[i],'', dividing2[i],'',cin,'',dividing3[i],'',cout)
        if (dividing1[i]==1) and (dividing2[i]==1): #다음 full adder의 올림값인 cin을 1로 정하기
            cin=1
        else:
            cin=0

    print('%d + %d = %04d + %04d = %04d' %(a,b,bina,binb,binab)) #4비트로 연산하기

print()
print('4비트 덧셈 연산')
total = 0
for i in range(0,8):
    total += i #누적변수 total
binnum = int(format(total, 'b')) #0~7까지의 합인 누적변수 total을 2진수로 변환하기
print("0+1+2+3+4+5+6+7 =",total, '=', binnum)
