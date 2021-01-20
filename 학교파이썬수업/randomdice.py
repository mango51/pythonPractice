import random

dice1, dice2, dice3, dice4, dice5, dice6 = [0] *6
throwCount, serialCount =0,0

if __name__ == '__main__':
    while True:
        throwCount += 1

        dice1= random.randrange(1,7)
        dice2 = random.randrange(1,7)
        dice3 = random.randrange(1,7)
        dice4 = random.randrange(1,7)
        dice5 = random.randrange(1,7)
        dice6 = random.randrange(1,7)

        if dice1==dice2==dice3==dice4==dice5==dice6:
            print('6개 주사위 숫자 동일함 : ',dice1, dice2, dice3, dice4, dice5,dice6)
            break
        elif (dice1==1 or dice2==1 or dice3 == 1 or dice4==1 or dice5==1 or dice6==1) and \
             (dice1==2 or dice2==2 or dice3 == 2 or dice4==2 or dice5==2 or dice6==2) and \
             (dice1==3 or dice2==3 or dice3 == 3 or dice4==3 or dice5==3 or dice6==3) and \
             (dice1==4 or dice2==4 or dice3 == 4 or dice4==4 or dice5==4 or dice6==4) and \
             (dice1==5 or dice2==5 or dice3 == 5 or dice4==5 or dice5==5 or dice6==5) and \
             (dice1==6 or dice2==6 or dice3 == 6 or dice4==6 or dice5==6 or dice6==6) :
             serialCount +=1
# 위의 코드는 각 주사위당 서로 다른 숫자가 나올 때 횟수 serialCount로 세기
# 서로 다른 숫자가 안나올 때는 실행할 수 없음
# 예를 들면 1,2,2,3,4,5가 나왔을 때는 True(1) and True(2,2) and True(3) and True(4) and True(5) and False(없음)
# 위와 같이 나오면 1 and 1 and 1 and 1 and 1 and 0 = 0 (False)로 나와서 실행 안 됨 ( 1 and 0 = 0 임)
    print('6개가 동일한 숫자가 나올 때까지, 주사위 던진 횟수 : ', throwCount)
    print('6개가 동일한 숫자가 나올 때까지, 1~6의 연속 변호가 나온 횟수 : ', serialCount)




